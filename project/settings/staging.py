import os
from project.settings.base import *

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

ALLOWED_HOSTS = ['.execute-api.us-east-1.amazonaws.com', '.amplifyapp.com']

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
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

# BOILERPLATE Modify the app base url to allow calls from the Local webapp
CORS_ORIGIN_REGEX_WHITELIST = (
    r'^(https?:\/\/)?(\w+\.)?localhost(:8000)?$',
    r'^(http?:\/\/)?(\w+\.)?localhost(:3000)?$',
    r'^(http?:\/\/)?(\w+\.)?127.0.0.1(:3000)?$',
    r'^(https?:\/\/)?staging.?(\w+\.)?amplifyapp\.com$'
)
