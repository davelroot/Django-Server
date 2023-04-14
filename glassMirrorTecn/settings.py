from django.contrib.messages import constants
from django.conf.locale.en import formats as en_formats
from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-umffx#w8nhk4r+_pxtmvus6c_0&^+3^@ph&)rq$%04x2ynbdf#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '0.0.0.0',
    '127.0.0.1',
    '192.168.121.130',
    'localhost',
    'glassmirrortecnologicia.com',
    #'glassmirrorconducaoformacao.co.ao',
    '*'
]

# Application definition

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.sites", # new
    # Third-party

    'tailwind',
    'theme',

    "crispy_forms",
    "crispy_bootstrap5",
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',  
    
# Application Externas  
    #'rolepermissions',
    #'rest_framework',
    'debug_toolbar',
    'taggit',
    'accounts.apps.AccountsConfig',
    ########################3
    'glassapi',
    ########################3
    'markeplace',
    ########################3
    'cursoAll',
    ########################3
    'mainHome',
    ########################3
        
]

TAILWIND_APP_NAME = 'theme'

NPM_BIN_PATH = '/usr/bin/npm'

# for permission management
#ROLEPERMISSIONS_MODULE = 'baseraiz.roles'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

MIDDLEWARE.insert(2, 'debug_toolbar.middleware.DebugToolbarMiddleware')


ROOT_URLCONF = 'glassMirrorTecn.urls'

AUTH_USER_MODEL = "accounts.User"

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend", # new
)

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

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#DATABASES = {
#	'default':{
#	'ENGINE': 'django.db.backends.mysql',
#	'NAME':'escoladeconducao',
#	'USER':'root',
#   'PASSWORD':'1q2w3e4r',
#    'HOST':'localhost',
#    'PORT':'3306',
#    	}
#    }
# --- PostgreSQL Development and production with db data--- #
# DATABASES = {
# 		'default': {
# 			'ENGINE': 'django.db.backends.postgresql',
# 			'NAME': config('NAME_DB'),
# 			'USER': config('USER_DB'),
# 			'PASSWORD': config('PASSWORD_DB'),
# 			'HOST': config('HOST_DB'),
# 			'PORT': config('PORT_DB'),
# 		}
# 	}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-pt'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'







# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-fieldl
# --- Custom User Model --- #
#AUTH_USER_MODEL = 'accounts.CustomUser'

#ROLEPERMISSIONS_MODULE = 'admin_tools.roles'
#ROLEPERMISSIONS_MODULE = "permissions.roles"
#LOGIN_URL = 'loginDG'
#LOGIN_URL = 'loginAlunos'
#LOGIN_URL = 'loginSecret'
#LOGIN_URL = 'loginProff'
# --- Login Logout User --- #
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = ''
LOGOUT_REDIRECT_URL = ''
ACCOUNT_LOGOUT_ON_GET = True

#LOGOUT_REDIRECT_URL = 'index'

SITE_ID = 1

# ----------------------------------------------------------
# Mensagens
MESSAGE_TAGS = {
	constants.ERROR: 'alert-danger',
	constants.WARNING: 'alert-warning',
	constants.DEBUG: 'alert-info',
	constants.SUCCESS: 'alert-success',
	constants.INFO: 'alert-info',
}

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


STRIPE_PUBLIC_KEY = ('STRIPE_TEST_PUBLIC_KEY')
STRIPE_SECRET_KEY = ('STRIPE_TEST_SECRET_KEY')
