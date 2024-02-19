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
DEBUG = False


ALLOWED_HOSTS = ['127.0.0.1','.vercel.app','localhost'] # Allow *.vercel.app

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }

# Application definition
# 'django_extensions',
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "surveyapp",
    "tailwind",
    "storages",
    'compressor',
    'django.contrib.sites',
    'social_django',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'debug_toolbar'
    # 'allauth.socialaccount.providers.openid'
]

SITE_ID = 2
SOCIALACCOUNT_LOGIN_ON_GET=True

ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_USERNAME_REQURIED=True

COMPRESS_URL = "/static/"
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
     'debug_toolbar.middleware.DebugToolbarMiddleware',
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
        }


AWS_STORAGE_BUCKET_NAME= 'survey-site-django-nicolas'
AWS_S3_REGION_NAME = 'us-east-1'
AWS_ACCESS_KEY_ID =     'AKIAZ2VRG6CP2YYH2NRZ'
AWS_SECRET_ACCESS_KEY= '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'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_DEFAULT_ACL= None




#ACCOUNT_DEFAULT_HTTP_PROTOCOL='https'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

LOGIN_URL = '/accounts/login/'

# AUTH_PARAMS['access_type']

ROOT_URLCONF = "djangosurvey.urls"

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

AWS_S3_SECURE_URLS = True
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
#STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR

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

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

# def show_toolbar(request):                                     # <-- NEW
#     return True                                                # <-- NEW 

# DEBUG_TOOLBAR_CONFIG = {                                       # <-- NEW
#     "SHOW_TOOLBAR_CALLBACK" : show_toolbar,                    # <-- NEW
# }                                                              # <-- NEW

# if DEBUG:                                                      # <-- NEW
#     import mimetypes                                           # <-- NEW          
#     mimetypes.add_type("application/javascript", ".js", True) 



# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'URL': env('DATABASE_URL'),
#         'NAME': env('PGDATABASE'),
#         'USER': 'postgres',
#         'PASSWORD': env('PGPASSWORD'),
#          'HOST': env('PGHOST'),
#          'PORT': 7723,
#     }
# }


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


SOCIAL_AUTH_GITHUB_KEY = env("SOCIAL_AUTH_GITHUB_KEY")
SOCIAL_AUTH_GITHUB_SECRET = env("SOCIAL_AUTH_GITHUB_SECRET")
#ACCOUNT_EMAIL_VERIFICATION = 'none'

# DEBUG_TOOLBAR_PANELS = [
#     'debug_toolbar.panels.versions.VersionsPanel',
#     'debug_toolbar.panels.timer.TimerPanel',
#     'debug_toolbar.panels.settings.SettingsPanel',
#     'debug_toolbar.panels.headers.HeadersPanel',
#     'debug_toolbar.panels.request.RequestPanel',
#     'debug_toolbar.panels.sql.SQLPanel',
#     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#     'debug_toolbar.panels.templates.TemplatesPanel',
#     'debug_toolbar.panels.cache.CachePanel',
#     'debug_toolbar.panels.signals.SignalsPanel',
#     'debug_toolbar.panels.logging.LoggingPanel',
#     'debug_toolbar.panels.redirects.RedirectsPanel',
# ]