
from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env("DJANGO_SECRET_KEY")
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]
# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {"default": {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": env.db("AWS_RDS_NAME"),
    "USER": env.db("AWS_RDS_USER"),
    "PASSWORD": env.db("AWS_RDS_PASSWORD"),
    "HOST": env.db("AWS_RDS_HOST"),
    "PORT": env.db("AWS_RDS_PORT"),
}}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
