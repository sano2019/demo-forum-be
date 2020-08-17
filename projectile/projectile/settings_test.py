# -*- coding: utf-8 -*-
from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_db',
        'TEST': {'NAME': 'test_db'},
    }
}

MIGRATION_MODULES = {
    'auth': None,
    'admin': None,
    'contenttypes': None,
    'reversion': None,
    'sessions': None,
    'sites': None,
    'accounting': None,
    'core': None,
    'e2eutils': None,
}

PASSWORD_HASHERS = ("django.contrib.auth.hashers.MD5PasswordHasher",)
