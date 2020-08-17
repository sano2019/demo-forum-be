import logging
from urllib.parse import quote, quote_plus

from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.contrib.auth.tokens import default_token_generator
from django.core import mail
from django.conf import settings as django_settings

from djoser import utils
from djoser.conf import settings
from rest_framework_jwt.settings import api_settings

from common.helpers.email import send_email_helper

logger = logging.getLogger(__name__)

# NOTE: BaseEmailMessage from django-templated-mail doesn't seem to
# work with Anymail's Mandrill integration because it defines
# a `template_name` class attribute. Anymail interprets this attribute
# as as a Mandrill template name and tries to pass it on to the
# Mandrill API, whereupon the request fails with an "unknown template"
# error. As a solution, I've reimplemented the core functionality
# of some of the Djoser emails manually.
