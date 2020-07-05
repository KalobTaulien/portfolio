from .base import *

DEBUG = False
SECRET_KEY = '+c*0b=u(=8i&(sbvaklk2aazwk)_mej7r5%-cs$uhbexv5*c4o'
ALLOWED_HOSTS = ['kalob.io']

cwd = os.getcwd()
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache"
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'portfolio',
        'USER': 'portfolio',
        'PASSWORD': '8##j56J#9jh3V2PGq#Wq',
        'HOST': 'localhost',
        'PORT': '',
    }
}

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://ebadb0c0953b481b87de51b13a5106bc@o416309.ingest.sentry.io/5310350",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

try:
    from .local import *
except ImportError:
    pass
