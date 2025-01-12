"""
Django settings for myinnstant project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import dj_database_url
import os
from django.test.runner import DiscoverRunner
from pathlib import Path
import cloudinary_storage

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

IS_HEROKU = "DYNO" in os.environ


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-os10bljw*w%mc^gi_cubz9r$&c*lef9c%+xrtc=@d8-59$0_+c'

if 'SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ["SECRET_KEY"]


# Generally avoid wildcards(*). However since Heroku router provides hostname validation it is ok

# ssl switch
# SECURE_SSL_REDIRECT = False
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',

    'innstant',
    'members',
    'django_filters',
    'crispy_forms',
    'autocomplete_light',
    'fontawesomefree',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myinnstant.urls'

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
                'innstant.context_processors.is_read_count_admin',
                'innstant.context_processors.is_read_count_tenant',
                'innstant.context_processors.footer',
            ],
        },
    },
]

WSGI_APPLICATION = 'myinnstant.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'dormks',
#         'USER': 'dormitoryks',
#         'PASSWORD': 'ksdormitory123',
#         'HOST': 'ksdata.cobjgmfi4r80.ap-southeast-2.rds.amazonaws.com',
#         'PORT': '5432'
#     }
# }

# DATABASES = {
#     'default': {
#         "ENGINE" : "django.db.backends.postgresql_psycopg2",
#         'NAME': 'ddpfmqesoehqd7',
#         'USER': 'sxwpjmdyeyxqiy',
#         'PASSWORD': '1b377774a0442ca9feb5dd547be8ec6babfe2b22226b5711310831831bb6fdf3',
#         'HOST': 'ec2-3-232-103-50.compute-1.amazonaws.com',
#         'PORT': '5432'
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/



STATIC_URL = '/static/'

STATICFILES_DIRS =[
    os.path.join(BASE_DIR, 'static')
]


STATIC_ROOT =  os.path.join(BASE_DIR, 'staticfiles') 
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
MEDIA_URL = '/images/'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'devqjzqxb',
    'API_KEY': '387258877532774',
    'API_SECRET': 'nTOb5YOLRBGjp2eJLYZYycsg_cY'
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.RawMediaCloudinaryStorage'

# Test Runner Config
class HerokuDiscoverRunner(DiscoverRunner):
    """Test Runner for Heroku CI, which provides a database for you.
    This requires you to set the TEST database (done for you by settings().)"""

    def setup_databases(self, **kwargs):
        self.keepdb = True
        return super(HerokuDiscoverRunner, self).setup_databases(**kwargs)


# Use HerokuDiscoverRunner on Heroku CI
if "CI" in os.environ:
    TEST_RUNNER = "myinnstant.settings.HerokuDiscoverRunner"


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'dormitoryks@gmail.com'
EMAIL_HOST_PASSWORD = 'yhxlomokjaxvyohk'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
