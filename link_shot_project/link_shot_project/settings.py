import os
import dotenv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

dotenv.load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure')

DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'link_shot_app.apps.LinkShotAppConfig',
    'accounts.apps.AccountsConfig',
    'six'
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

ROOT_URLCONF = 'link_shot_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'link_shot_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get("SQL_ENGINE", 'django.db.backends.sqlite3'),
        'NAME': os.environ.get("DB_NAME", BASE_DIR / 'db.sqlite3'),
        'USER': os.environ.get("DB_USER", "user"),
        'PASSWORD': os.environ.get("DB_PASS", "password"),
        'HOST': os.environ.get("DB_HOST", "localhost"),
        'PORT': os.environ.get("DB_PORT", "5432"),
    }
}

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Minsk'

USE_I18N = True

USE_TZ = True

STATIC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    STATIC_PATH,
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_REDIRECT_URL = 'info'

LOGOUT_REDIRECT_URL = 'info'
