"""
Django settings for alumnos project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '()mlt0mae5r!$qn1hs5kz1a&x@k*d+)fk9iu$8jx9-kk$)hx4x'
SECRET_KEY = config('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
<<<<<<< HEAD
# DEBUG = False
DEBUG = config('DEBUG', default=False, cast=bool)
=======
DEBUG = True

ALLOWED_HOSTS = ['34.224.93.86']
>>>>>>> staging

# ALLOWED_HOSTS = ['172.31.22.225']
ALLOWED_HOSTS = ["*",'34.224.93.86']

# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
    'rest_framework.authtoken',
    'corsheaders',
    #---------------------------------------
     'rest_auth',
     'rest_auth.registration',
     'allauth',
      'allauth.account',
      'allauth.socialaccount',
]
#-------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ]
}
#-------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    
]

# CORS_ORIGIN_WHITELIST = (
#   'http://localhost:4200',
#   'http://127.0.0.1:4200',
# )

CORS_ORIGIN_WHITELIST = (
  'http://localhost:4200',
  'http://ec2-34-224-93-86.compute-1.amazonaws.com',
  'http://127.0.0.1:4200',
  'http://34.224.93.86',
  'http://alumnosweb.ddns.net:4200',
)

ROOT_URLCONF = 'alumnos.urls'

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

WSGI_APPLICATION = 'alumnos.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#   DATABASES={
#       'default': {
#           'ENGINE': 'django.db.backends.postgresql_psycopg2',
#           'NAME': 'Back_reporte',
#           'USER': 'postgres',
#           'PASSWORD': 'angel20340',
#           'HOST': '127.0.0.1',
#           'PORT': '5432',
#       }
#     }
DATABASES={
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'webdb',
        'USER': 'webuserdb',
        'PASSWORD': 'angel20340',
        'HOST': '34.224.93.86',
        'PORT': '5432',
    }
}
#  DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.postgresql_psycopg2',
#          'NAME': 'webdb',
#          'USER': 'webuserdb',
#          'PASSWORD': 'angel20340',
#          'HOST': '172.31.22.225',
#          'PORT': '5432',
#      }
#  }

<<<<<<< HEAD
 DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'webdb',
         'USER': 'webuserdb',
         'PASSWORD': 'angel20340',
         'HOST': '172.31.22.225',
         'PORT': '5432',
     }
 }

=======
>>>>>>> staging
# import dj_database_url
# from decouple import config

# DATABASES = {
#      'default': dj_database_url.config(
#          default=config('DATABASE_URL')
#      )
# }


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

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#     OS.path.join(BASE_DIR, 'static'),
# )

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# REST_FRAMEWORK = {
#   'DEFAULT_PERMISSION_CLASSES': [                     
#     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
#   ],
# }

SITE_ID = 1

ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False

AUTHENTICATION_BACKENDS = (
   "django.contrib.auth.backends.ModelBackend",
   "allauth.account.auth_backends.AuthenticationBackend"
)


try: 
    from alumnos.local_settings import *
except ImportError:
    pass    