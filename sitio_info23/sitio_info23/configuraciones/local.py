from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'sitio_info23db',
        "USER": "root",
        "PASSWORD": "Hdd35469880",
        'HOST': 'localhost',
        'PORT': 3306,
    }
}

