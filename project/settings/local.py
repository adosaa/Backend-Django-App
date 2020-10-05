import os
from project.settings.base import *

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

ALLOWED_HOSTS = ['.local', '.test', '127.0.0.1', '.localhost']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': os.getenv("DB_ENGINE"),
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT")
    }
}
