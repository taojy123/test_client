"""
Django settings for test_client project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd#*x#0)yvi^lcm9ctl5gd0j(ym+gfi9-o85ptyze@q)mgticpe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_sanction',
    'client',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'test_client.urls'

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

WSGI_APPLICATION = 'test_client.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'



SANCTION_PROVIDERS = {
    'weibo': {
        'auth_endpoint': 'https://api.weibo.com/oauth2/authorize',
        'token_endpoint': 'https://api.weibo.com/oauth2/access_token',
        'resource_endpoint': 'https://api.weibo.com/oauth2',
        'scope': 'email',
        'client_id': '3294908720',
        'client_secret': '758c4426b8d32df06a62166d49e34bb2',
        'redirect_uri': 'http://taojy123.com:8080/client/o/login/weibo',
    },
    'local': {
        'auth_endpoint': 'http://127.0.0.1:8000/api/oauthadmin/authorize/',
        'token_endpoint': 'http://127.0.0.1:8000/api/oauthadmin/token/',
        'resource_endpoint': 'http://127.0.0.1:8000/api',
        'scope': 'article:read article:write',
        'client_id': 'NwMiG3xolPXSG5ZK24R5FPWETDYmHj0Cr5mOjRd4',
        'client_secret': 'X0GIDDIXQVEil7zgEoY2tfLJNdIo1PPhmsPQEaVOaEElVmKWSB6urgLSGYgPJ9AzQjIY41pj7IRWVASp2kGB3ZpDdLZK3IwJcirV3ZV6bU27sZrsZPQm2IHQ7xchY6Ib',
        'redirect_uri': 'http://127.0.0.1:8080/client/o/login/local/',
    },
    'heyshop': {
        'auth_endpoint': 'http://demo.xiaoheidian.com/api/oauthadmin/authorize/',
        'token_endpoint': 'http://demo.xiaoheidian.com/api/oauthadmin/token/',
        'resource_endpoint': 'http://demo.xiaoheidian.com/api',
        'scope': 'article:read article:write',
        'client_id': 'hY6HBpl4Qj5nHOS9DkKxybh2WDiLvQPGAX0EVvtS',
        'client_secret': 'LAGc6FiK4YexPrGB1GZJcnJDjPiBTFN4BYLt7MRDCbxsYyrTOdFM6TYof8tP1JZXzCyXrQSK6MgaHSIsULiinEi1sfDzs4SLk9PAqFXVOud7vZ06Fu8L0ziA1FsTfjQ6',
        'redirect_uri': 'http://demo.xiaoheidian.com/client/o/login/heyshop/',
    },
}

AUTH_USER_MODEL = 'client.User'

AUTHENTICATION_BACKENDS = (
    'django_sanction.backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = '/client/'
LOGIN_REDIRECT_URL = '/client/profile/'
# SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

MIDDLEWARE_CLASSES = MIDDLEWARE