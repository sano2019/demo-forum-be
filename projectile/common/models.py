import os
import uuid
from django.db import models
from django.contrib.admin import SimpleListFilter
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from common.managers import SoftDeleteManager

IMAGE_ASPECT_RATIO_TEXT = _(
    'The Aspect Ratio should be 16:9. Image will be cropped/resized otherwise.'
)


class AbstractContactModel(models.Model):
    def get_file_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join('user_images', filename)

    phone_number = models.CharField(max_length=30, null=True, blank=True)
    first_name = models.CharField(max_length=130, blank=True)
    last_name = models.CharField(max_length=130, blank=True)
    title = models.CharField(max_length=127, blank=True, null=True)
    image = models.ImageField(
        upload_to=get_file_path,
        null=True,
        blank=True,
        help_text=_(
            'The Aspect Ratio should be 1:1. Image will be cropped/resized otherwise'
        ),
    )

    class Meta:
        abstract = True

    def get_full_name(self):
        name = u'{} {}'.format(self.first_name, self.last_name)
        return name.strip()

    def get_short_name(self):
        return u'{}'.format(self.email)


class AbstractOrganisationModel(models.Model):
    website = models.URLField(null=True, blank=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    info = models.TextField(
        null=True,
        blank=True,
        help_text='List organisations business hours, telephone number, address etc',
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text='Description of what the organisation does',
    )
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True


class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()
    all_objects = SoftDeleteManager(alive_only=False)

    class Meta:
        abstract = True

    def hard_delete(self):
        super(SoftDeleteModel, self).delete()

    def delete(self):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save(update_fields=['deleted_at', 'is_deleted'])

    def restore(self):
        self.deleted_at = None
        self.is_deleted = False
        self.save(update_fields=['deleted_at', 'is_deleted'])


class SoftDeleteFilter(SimpleListFilter):
    title = 'deleted'
    parameter_name = 'deleted'

    def lookups(self, request, model_admin):
        return (('deleted', ('Deleted')),)

    def queryset(self, request, queryset):
        if self.value() == 'deleted':
            return queryset.filter(is_deleted=True)
        else:
            return queryset.filter(is_deleted=False)
