"""
Django settings for projectile project.

Generated by 'django-admin startproject'.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import datetime

import dj_database_url
from dotenv import load_dotenv

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# The root of the git repo - Could be ~/project or ~/repo
REPO_DIR = os.path.realpath(os.path.join(BASE_DIR, '..'))
# The directory of the current user ie /home/django a.k.a. ~
HOME_DIR = os.path.realpath(os.path.join(REPO_DIR, '..'))

# Load environment variables - see https://12factor.net/
load_dotenv(dotenv_path=os.path.join(REPO_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w&=lrxp97l$+sx(xx@89l4w0%_e!kx0ho75krdj-#pca%xu1=p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SITE_ID = 1

ADMINS = (('Hassan Mian', 'mian@willandskill.se'),)

ALLOWED_HOSTS = [
    'yoshi.willandskill.eu',
    '192.168.1.11',
    'testserver',
    'localhost'
]

INTERNAL_IPS = []

# Application definition

INSTALLED_APPS = [
    'forum.apps.ForumConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'djoser',
    'drf_yasg',
    'corsheaders',
    'anymail',
    'reversion',
    'django_extensions',
    'markdownx',
    'common',
    'e2eutils',
    'core',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'core.middleware.DynamicOrganisationIDMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'projectile.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    }
]

WSGI_APPLICATION = 'projectile.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# CREATE USER demoforum WITH PASSWORD 'supersecret';
# CREATE DATABASE demoforum;
# GRANT ALL PRIVILEGES ON DATABASE demoforum to demoforum;

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'demo-forum-db',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 5,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Stockholm'

USE_I18N = True

USE_L10N = True

USE_TZ = False

USE_THOUSAND_SEPARATOR = True

AUTH_USER_MODEL = 'core.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

STATIC_ROOT = '/home/django/staticfiles/'
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(HOME_DIR, 'media')
MEDIA_URL = '/media/'

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': (
        'rest_framework.pagination.PageNumberPagination'
    ),
    'PAGE_SIZE': 5,
}

PASSWORD_RESET_TIMEOUT_DAYS = 90

# JWT SETTINGS
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=365),
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=365),
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}

# CLIENT SETTINGS
CLIENT_URI = 'http://localhost:3000'

# EMAIL SETTINGS
ANYMAIL = {
    'MANDRILL_API_KEY': os.environ.get(
        'MANDRILL_API_KEY', 'pQsFOHbORGsLylZ2xte0mQ'
    )
}
# EMAIL_BACKEND = 'anymail.backends.mandrill.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'no-reply@demo-forum.com'
SERVER_EMAIL = 'no-reply@demo-forum.com'

# DJOSER SETTINGS
DJOSER = {
    'ACTIVATION_URL': CLIENT_URI
    + '/register/activate?uid={uid}&token={token}',
    'ACTIVATION_URI': '/register/activate?uid={uid}&token={token}',
    # NOTE: INVITATION_URL is our custom setting
    'INVITATION_URL': CLIENT_URI + '/register/acceptInvite?uid={uid}&token={token}&email={email}',
    'INVITATION_URI': '/register/acceptInvite?uid={uid}&token={token}&email={email}',
    'PASSWORD_RESET_CONFIRM_URL': CLIENT_URI
    + '/login/confirm-reset-password?uid={uid}&token={token}&email={email}',
    'PASSWORD_RESET_CONFIRM_URI': '/login/confirm-reset-password?uid={uid}&token={token}&email={email}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {
        'user_create': 'core.serializers.CreateUserSerializer',
        'current_user': 'core.serializers.MiniUserSerializer',
    },
    'EMAIL': {
        'activation': 'core.emails.ActivationEmail',
        'password_reset': 'core.emails.PasswordResetEmail',
    },
    'PERMISSIONS': {
        'user_create': ['rest_framework.permissions.IsAdminUser'],
        'set_username': ['rest_framework.permissions.IsAdminUser'],
        'user_list': ['rest_framework.permissions.IsAdminUser'],
        'user_delete': ['rest_framework.permissions.IsAdminUser'],
        'username_reset': ['rest_framework.permissions.IsAdminUser'],
        'username_reset_confirm': ['rest_framework.permissions.IsAdminUser'],
    },
}


def organisation_request_callback(request):
    pass


# Logging settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'main_formatter'
        },
    },
    'loggers': {
        '': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
            'formatter': 'simple',
        },
        'default': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG'
        }
    },
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S",
        },
        'simple': {'format': '%(levelname)s %(message)s'},
        'main_formatter': {
            'format': '%(levelname)s:%(name)s: %(message)s '
            '(%(asctime)s; %(filename)s:%(lineno)d)',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
        'message_and_time_formatter': {
            'format': '%(asctime)s, %(lineno)d: %(message)s ',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
    },
}

SWAGGER_SETTINGS = {'VALIDATOR_URL': None}

sentry_sdk.init(
    os.environ.get("SENTRY_DSN", ""),
    environment=os.environ.get("SENTRY_ENVIRONMENT", "dev"),
    integrations=[DjangoIntegration()],
)

FILE_UPLOAD_PERMISSIONS = 0o644

LOCIZE_PROJECT_ID = "8f96f7b4-aa3e-4376-95f0-7208f52224d5"
