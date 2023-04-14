from django.contrib.messages import constants
from django.conf.locale.en import formats as en_formats
from pathlib import Path
import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = config('SECRET_KEY')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   # Third-party
    'tailwind',
    'theme',
    "crispy_forms",
    "crispy_bootstrap5",   
    
# Application Externas  
    #'rolepermissions',
    #'rest_framework',
    'debug_toolbar',
    'taggit',
    'accounts.apps.AccountsConfig',    

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'django_countries',

    ########################3
    'glassapi',
    ########################3
    'markeplace',
    ########################3
    'cursoAll',
    ########################3
]

TAILWIND_APP_NAME = 'theme'

NPM_BIN_PATH = '/usr/bin/npm'

MIDDLEWARE = [
    
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'glassMirrorTecn.urls'

AUTH_USER_MODEL = "accounts.User"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend" # 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ACCOUNT_USERNAME_REQUIRED = False # new
ACCOUNT_AUTHENTICATION_METHOD = "email" # new
ACCOUNT_EMAIL_REQUIRED = True # new
ACCOUNT_UNIQUE_EMAIL = True # new
EMAIL_USE_TLS = True
EMAIL_HOST = "email_host"
EMAIL_PORT = "email_port"
EMAIL_HOST_USER = "email_host_user"
EMAIL_HOST_PASSWORD = "email_host_password"
DEFAULT_FROM_EMAIL = "default_from_email"


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'glassMirrorTecn.wsgi.application'

# django-crispy-forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5" # new
CRISPY_TEMPLATE_PACK = "bootstrap5"

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

# Auth

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)
SITE_ID = 1

MESSAGE_TAGS = {
	constants.ERROR: 'alert-danger',
	constants.WARNING: 'alert-warning',
	constants.DEBUG: 'alert-info',
	constants.SUCCESS: 'alert-success',
	constants.INFO: 'alert-info',
}


LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = ''
LOGOUT_REDIRECT_URL = ''
ACCOUNT_LOGOUT_ON_GET = True
# CRISPY FORMS

TAGGIT_CASE_INSENSITIVE = True

DOMAIN = ''

SECURE_CROSS_ORIGIM_OPENER_POLICY = 'unsafe-none'

ATOMIC_REQUESTS = True

MAX_UPLOAD_SIZE = 5242880

FILE_UPLOAD_PERMISSIONS = 0o640

en_formats.DATE_FORMAT = 'd-m-Y'
en_formats.DATETIME_FORMAT = 'd-m-Y H:i:s'
en_formats.DATE_INPUT_FORMATS = ['%d-%m-%Y']
en_formats.DATETIME_INPUT_FORMATS = ['%d-%m-%Y %H:%i:%s']

#AUTH_USER_MODEL = 'staff.Staff'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_AGE = 60*60*24  # 24 hours

# SHOP SETTINGS
PRINT_RECEIPTS = True