# flake8: noqa
# isort: skip_file
# type: ignore
import redis

from .base_conf._base import *

RUN_DAP_PROCESS = config('RUN_DAP_PROCESS', default=False, cast=bool)

LOCAL_BASE_DIR = BASE_DIR.parent.parent.joinpath('local-dev')

DEBUG = True
SECRET_KEY = "SECRET"
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=lambda v: [s.strip() for s in v.split(',')])

DATABASES['default'] = {
    "ENGINE": 'django.db.backends.postgresql',
    'USER': 'dev-jw',
    'PASSWORD': 'dev-jw',
    'HOST': 'localhost',
    'PORT': '5432',
}
