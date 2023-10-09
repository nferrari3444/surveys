"""
Django settings for djangosurvey project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import environ
from django.contrib.messages import constants as messages
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-oqj1+ec6=nf-06m+hd7qb*3mbky!a1eq1inp0x6%)q(6a4b5^b"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []





MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django_extensions',
    "surveyapp",
    "tailwind",
    'compressor',
    'django.contrib.sites',
    'social_django',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.openid'
    
]

SITE_ID = 2
SOCIALACCOUNT_LOGIN_ON_GET=True

ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_USERNAME_REQURIED=True

COMPRESS_ROOT = BASE_DIR / 'static'

COMPRESS_ENABLED = True

STATICFILES_FINDERS = ('compressor.finders.CompressorFinder',)

# TAILWIND_APP_NAME = 'theme'
# INTERNAL_IPS = ["127.0.0.1",]
# NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
     'social_django.middleware.SocialAuthExceptionMiddleware',
     
    #  "django_browser_reload.middleware.BrowserReloadMiddleware",
]

# AUTH_USER_MODEL = "user.User"




SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online', # se cambia de online a offline(To refresh authentication in the background)
        },

        "APP": {
            "client_id": env("GOOGLE_CLIENT_ID"),
            "secret": env("GOOGLE_CLIENT_SECRET"),
        },
    } ,
  
    # 'facebook': {
    # 'METHOD': 'js_sdk', 
    #  'SCOPE': ['email', 'public_profile', 'user_friends'], 
    #  'AUTH_PARAMS': {'auth_type': 'reauthenticate'}, 
    #  'INIT_PARAMS': {'cookie': True},
    #  'FIELDS': [
    #      'id',
    #      'email',
    #      'name',
    #      'first_name',
    #      'last_name',
    #      'verified',
    #      'locale',
    #      'timezone',
    #      'link',
    #      'gender',
    #      'updated_time'],
    #      'EXCHANGE_TOKEN': True,
    #      'LOCALE_FUNC': lambda request: 'en_US',
    #      'VERIFIED_EMAIL': False,
    #      'VERSION':' V2.4',
         
           
    #   'APP': {
    #          'client_id': env("SOCIAL_AUTH_FACEBOOK_KEY"),  # !!! THIS App ID
    #          'secret': env("SOCIAL_AUTH_FACEBOOK_SECRET"),
    #           'key':''  # !!! THIS App Secret              'key': ''
    #              },    
                
    #     }
        
        }


#facebook
SOCIAL_AUTH_FACEBOOK_KEY = env("SOCIAL_AUTH_FACEBOOK_KEY")  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = env("SOCIAL_AUTH_FACEBOOK_SECRET")#app key


#ACCOUNT_DEFAULT_HTTP_PROTOCOL='https'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

LOGIN_URL = '/accounts/login/'

# AUTH_PARAMS['access_type']

ROOT_URLCONF = "djangosurvey.urls"

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
                 'social_django.context_processors.backends',
                 
            ],
        },
    },
]

WSGI_APPLICATION = "djangosurvey.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Redirect to home URL after login (Default redirects to /accounts/profile/)

#gmail_send/settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ferrarinicolas927@gmail.com'
EMAIL_HOST_PASSWORD =  env("EMAIL_HOST_PASSWORD") #past the key or password app here
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'default from email'
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTHENTICATION_BACKENDS = [
            'social_core.backends.github.GithubOAuth2',
          'django.contrib.auth.backends.ModelBackend',
           'allauth.account.auth_backends.AuthenticationBackend',
            
            'social_core.backends.facebook.FacebookOAuth2',
  

]

#for extra info
SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'email',
]


SOCIAL_AUTH_GITHUB_KEY = 'acefef149cac0f5462b8'
SOCIAL_AUTH_GITHUB_SECRET = '0a2799d429d1b1ab27293248d62305e46d8c9ee8'

#ACCOUNT_EMAIL_VERIFICATION = 'none'


