"""
Django settings for EmotionDiary project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
import pymysql    # 一定要加
pymysql.install_as_MySQLdb()   # 一定要加

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# master-----------------------------------------------------------
LINE_CHANNEL_ACCESS_TOKEN = 'r5fMBbir3iMPWiB5ljtrNFUZRNBKTDWHGp1bZRngaMwo2A1/U8EYpuAqPPXcgYMzGWgd7CtHasUVWfGzOWzJzkYROF9hueAr7593pIpZi9doAO2eM7hnSM+Tk/ucUXql+fFaD4rdl1bLUncwwAo8SwdB04t89/1O/w1cDnyilFU='
LINE_CHANNEL_SECRET = '4035572c42c59a932917e526f2ae1324'
SECRET_KEY = '*f60@damy%^)#)=$@+0804h=nvwyhi594_az@3oo=u$+u(pc&+'
# ----------------------------------------------------------------

# kelly-----------------------------------------------------------
# LINE_CHANNEL_ACCESS_TOKEN = '6pzegJmVUuwqq78rLWl87O9Tr5N8kNU7r8+kxhizZ2emhpTiWMt2OdBCnA19Xqi/nla5PeZNwO++cZYOMHDZKuCpezNxMVYbyDRK1g3RGemZD7XR09bIOaOW3uIBnpBga6XGUXS5M0smEIW4O32aHgdB04t89/1O/w1cDnyilFU='
# LINE_CHANNEL_SECRET = '60f84eb382e4db050cb164e0d0034b9f'
# SECRET_KEY = '*f60@damy%^)#)=$@+0804h=nvwyhi594_az@3oo=u$+u(pc&+'
# ----------------------------------------------------------------

# 16-----------------------------------------------------------
# LINE_CHANNEL_ACCESS_TOKEN = 'j7AojEDEFiURHXb+NCZRvtYlHaP8hSt7sLeMVDDlK/z3TambVgaTeYsUhk2134fpk9/V1/y0p9foMnlkD/p6yE5r2IHEjruHlgp931416eeWGu3iN5xF4D1MZOAJvUv/nWmRfAIdm4GXUldTb+7oCQdB04t89/1O/w1cDnyilFU='
# LINE_CHANNEL_SECRET = '22b5a8ab0ef1feff4475994dbdaf61d3'
# SECRET_KEY = '*f60@damy%^)#)=$@+0804h=nvwyhi594_az@3oo=u$+u(pc&+'
# -------------------------------------------------------------

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SET_URL = '2661aaf0c7ff.ngrok.io'
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',
    'AI_analyze',
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

ROOT_URLCONF = 'EmotionDiary.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'EmotionDiary.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # },
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 數據庫引擎
        'NAME': 'diary',  # DB名稱，ex: sakila
        'USER': 'root',     # 用戶名
        # 'PASSWORD': 'Imd@110208',  # local密碼
        'PASSWORD': 'mysql123',  # 140上mysql密碼
        'HOST': '127.0.0.1',  # 本機端ip
        'PORT': '3306',         # port
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
