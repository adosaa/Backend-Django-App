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
