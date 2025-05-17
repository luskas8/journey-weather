#flake8: noqa

from . import *

__all__ = [
    # 'AUTH_USER_MODEL',
    'BASE_DIR',
    'INSTALLED_APPS',
    # 'REST_FRAMEWORK',
    'TEMPLATES',
]

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',

    # External deps
    'rest_framework',

    # internal apps
    'core',
]

TEMPLATES = [ # type: ignore
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# AUTH_USER_MODEL = "db.Context"

# REST_FRAMEWORK = {
#     'EXCEPTION_HANDLER': 'core.handlers.custom_exception_handler'
# }
