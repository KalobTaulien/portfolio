from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5ichop1)r6^p(+pg%+y!6byyp$j_38sde16kpv&y#x276#rtc*'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '',
    }
}

INSTALLED_APPS += [
    'debug_toolbar',
    'wagtail.contrib.styleguide',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
    '172.17.0.1',
]

CACHES = {
    "default": {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
]
DEBUG_TOOLBAR_CONFIG = {
    'ENABLE_STACKTRACES': False,
    'PROFILER_MAX_DEPTH': 5,
    'SHOW_TEMPLATE_CONTEXT': False,
}

try:
    from .local import *
except ImportError:
    pass
