from .base import *  # noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY", default="b#-1)@q6z9a=(f6!drg##qj*60r(amfd)d!6_!_*a^a@m2n(a1"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

EMAIL_BACKEND = "djcelery_email.backends.Celery.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_PORT = "support@blogscribe.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Blogscribe"
