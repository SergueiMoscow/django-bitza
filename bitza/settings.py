import os
import sys
from pathlib import Path
from environs import Env
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
env = Env()
env.read_env(str(BASE_DIR / '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
print(ALLOWED_HOSTS)
# Application definition

INSTALLED_APPS = [
    'rent',
    'work',
    'electricity',
    'api',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # CORS
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'bitza.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'bitza.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

database_engine = env('DATABASE_ENGINE')
if database_engine.lower() == 'mysql':
    # Пока оставляем для обратной совместимости
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'read_default_file': os.path.join(BASE_DIR, "db.cnf"),
                "init_command": "SET default_storage_engine=INNODB; \
                    SET sql_mode='STRICT_TRANS_TABLES', innodb_strict_mode=1",
                'charset': 'utf8mb4',
                'use_unicode': True,
            }
        }
    }
elif database_engine.lower() == 'postgresql':
    database_schema = env('DATABASE_SCHEMA')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env('DATABASE_NAME'),
            'OPTIONS': {'options': f'-c search_path={database_schema}'},
            'USER': env('DATABASE_USER'),
            'PASSWORD': env('DATABASE_PASSWORD'),
            'HOST': env('DATABASE_HOST'),
            'PORT': env.int('DATABASE_PORT', 5432),
            'CONN_MAX_AGE': 300,
        },
    }
else:
    raise ValueError('Invalid database engine')

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

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
        sys.prefix + '/lib/python' + str(sys.version_info.major) + '.' + str(sys.version_info.minor) +
        '/site-packages/django/contrib/admin/static',
    )
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
# print(f'Static root {STATIC_ROOT}')
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/main'
MEDIA_ROOT = os.path.join(BASE_DIR, 'documents')
MEDIA_URL = '/documents/'
CSRF_TRUSTED_ORIGINS = env.list('TRUSTED_ORIGINS')
NORM_MONTH_KWT = env.int('NORM_MONTH_KWT', 80)

# myproject/settings.py

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),  # Время жизни access-токена
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),    # Время жизни refresh-токена
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
}

CORS_ALLOW_ALL_ORIGINS = True

# For debugging
# MIDDLEWARE += ['bitza.debug_requests.LogRequestsMiddleware']
REST_FRAMEWORK['EXCEPTION_HANDLER'] = 'bitza.debug_requests.custom_exception_handler'

BILLS_GRPC_SERVER_ADDRESS=env('BILLS_GRPC_SERVER_ADDRESS')
BILLS_SERVICE_TOKEN=env('BILLS_SERVICE_TOKEN')

DEPLOY_TOKEN=env('DEPLOY_TOKEN')
DEPLOY_ENDPOINT=env('DEPLOY_ENDPOINT')
