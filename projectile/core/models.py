import csv
import os
import uuid
from datetime import datetime

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import exceptions as core_exceptions
from django.db import models, transaction
from django.db.utils import DataError
from django.utils import timezone, translation
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_lazy as _

from common.models import (IMAGE_ASPECT_RATIO_TEXT, AbstractContactModel,
                           AbstractOrganisationModel, SoftDeleteModel)
from core.managers import UserManager
from enumerify import fields
from rest_framework.serializers import ValidationError

ERROR_TYPES = (ValidationError, core_exceptions.ValidationError)


class Country(models.Model):
    title = models.CharField(max_length=128)
    

class User(AbstractBaseUser, PermissionsMixin, AbstractContactModel):

    email = models.EmailField(_('email address'), unique=True, db_index=True)
    title = models.CharField(max_length=127, null=True, blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('May user log into this admin site?'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_('Unselect this instead of deleting accounts.'),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def __str__(self):
        return u'{} {}'.format(_('Email:'), self.email)

    def clean(self, *args, **kwargs):
        self.email = self.email.lower()
        return super(User, self).clean(*args, **kwargs)

    def get_user_language_code(self):
        if self.language:
            return self.language.code
        return 'en'
        # return translation.get_language()

    def check_onboarded_data_exists(self):
        if (
            self.first_name
            and self.last_name
            and self.title
            and self.phone_number
        ):
            return True
        return False


