from .base import *

DEBUG = False
SECRET_KEY = '+c*0b=u(=8i&(sbvaklk2aazwk)_mej7r5%-cs$uhbexv5*c4o'
ALLOWED_HOSTS = ['kalob.io', '142.93.87.56']

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

try:
    from .local import *
except ImportError:
    pass
