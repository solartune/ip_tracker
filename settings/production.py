from .base import *

DEBUG = False

SITE_NAME = 'sitename.com'

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = 'http://static.{}/static/'.format(SITE_NAME)

MEDIA_URL = 'http://media.{}/media/'.format(SITE_NAME)

PROJECT_HOST = 'http://{}'.format(SITE_NAME)

NO_REPLY_EMAIL = "noreply@{}".format(SITE_NAME)

SERVER_EMAIL = 'error@{}'.format(SITE_NAME)

ADMINS = (
    ('solartune', 'solartune@yandex.ru'),
)

MANAGERS = ADMINS

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler'
        },
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
    }
}
