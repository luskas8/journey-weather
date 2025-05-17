# flake8: noqa

from . import *

__all__ = [
    'MIGRATION_MODULES',
    'DEFAULT_AUTO_FIELD',
    'MIGRATION_LOCK_ID',
    'DATABASES',
    'CACHES',
]

# disable migrations for legacy models
MIGRATION_MODULES = {
    'reference_data': 'reference_data.base',
}

# Value used to lock database while a migration is being performed
MIGRATION_LOCK_ID = 314

# if strictly necessary, override this per-app basis, although
# we primarily will use surrogate keys for internal data access,
# and it is preferred to composite this key with a natural key
# instead of replacing it, if ever needed
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 'default' database has an insecure value, therefore the
# default config is environment-specific, so we only
# define the legacy databases connection strings here
# obs.: the conns here are from meta legacy compose
# https://docs.djangoproject.com/en/5.1/ref/databases/#postgresql-connection-settings
DATABASES = {}

# https://docs.djangoproject.com/en/5.1/topics/cache/#redis
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'django_cached_data',
    }
}
