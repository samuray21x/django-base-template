import os
import environ

root = environ.Path(__file__) - 4
public_root = root.path('public/')
env = environ.Env()
environ.Env.read_env()

SITE_ROOT = root()
STATIC_ROOT = public_root('static')
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = public_root('media')
MEDIA_URL = '/media/'

DEBUG = env.bool('DEBUG', default=False)
SECRET_KEY = env.str('SECRET_KEY')
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'whitenoise',

    # project apps
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
    'core.middleware.MainExceptionMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Logging
LOGS_ENABLED = not DEBUG
if LOGS_ENABLED:
    LOGS_DIR = SITE_ROOT + '/logs/'
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {pathname} func: {funcName} process:{process:d} thread:{thread:d} MESSAGE: {message}',
                'style': '{',
            },
            'simple': {
                'format': '{levelname} {message}',
                'style': '{',
            },
        },
        'handlers': {
            'debug_file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': LOGS_DIR + 'debug.log',
                'formatter': 'simple',
            },
            'info_file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': LOGS_DIR + 'info.log',
                'formatter': 'verbose'
            },
            'main_file': {
                'level': 'WARNING',
                'class': 'logging.FileHandler',
                'filename': LOGS_DIR + 'main.log',
                'formatter': 'verbose'
            },
        },
        'loggers': {
            'django': {
                'handlers': ['main_file'],
                'level': 'WARNING',
                'propagate': False,
            },
            'core': {
                'handlers': ['main_file'],
                'level': 'WARNING',
                'propagate': False,
            },
        },
    }
