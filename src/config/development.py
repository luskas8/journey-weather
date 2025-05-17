# flake8: noqa
# isort: skip_file
# type: ignore

from calendar import c
from email.policy import default
from .base_conf._base import *

# every config here should be overridable using config()
# for test and environment simulation porpouses

# start debugpy server
RUN_DAP_PROCESS = config('RUN_DAP_PROCESS', default=False, cast=bool)

SECRET_KEY = config('DJANGO_SECRET_KEY', default='insecure-secret-key')

# only use this when setting defaults for local development
LOCAL_BASE_DIR = BASE_DIR.parent.parent.joinpath('local-dev')

DEBUG = config('DJANGO_DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=lambda v: [s.strip() for s in v.split(',')])

# SQLite databases are auto-created at the first .connect() call,
# when using other DBMS you shold run a CREATE DATABASE script first
DATABASES['default'] = config(
    'DATABASE_URL',
    default='sqlite:///' + str(LOCAL_BASE_DIR.joinpath('db.sqlite3')),
    cast=db_url
)


# setting the middleware configuration
MIDDLEWARE.extend(
    [
        # 'api.auth.middlewares.auth.BypassAuthenticationMiddleware', # use this middleware to bypass something in local development
        'django.contrib.auth.middleware.AuthenticationMiddleware'
    ]
)

# Turn on OTEL
# from opentelemetry import trace
# from opentelemetry.exporter.otlp.proto.grpc import trace_exporter
# from opentelemetry.sdk import resources
# from opentelemetry.sdk import trace as trace_provider
# from opentelemetry.sdk.trace import export as trace_export
# # Configura envio dos dados para o OTLP
# LOGGING['handlers']['otlp'] = {
#     'level': 'INFO',
#     'class': 'config.logger.handlers.OTLPLoggingHandler',
# }
# LOGGING['root']['handlers'] = ["console", "otlp"]

# r = resources.Resource.create(attributes=OTEL_RESOURCE_ATTRIBUTES)
# tracer = trace_provider.TracerProvider(resource=r)
# tracer.add_span_processor(trace_export.BatchSpanProcessor(trace_exporter.OTLPSpanExporter()))
# trace.set_tracer_provider(tracer_provider=tracer)
