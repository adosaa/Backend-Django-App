import os
from project.core_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

INSTALLED_APPS = INSTALLED_APPS + [
    'django_backend_template',
    'rest_framework',
    'drf_yasg',
    'django_fullclean',
]

SITE_ID = 1

# rest-auth settings
REST_USE_JWT = True
OLD_PASSWORD_FIELD_ENABLED = True
LOGOUT_ON_PASSWORD_CHANGE = False

# Allauth settings
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 5
ACCOUNT_USERNAME_BLACKLIST = ['admin', 'Admin', 'Administrator', 'administrator']

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend"
)
