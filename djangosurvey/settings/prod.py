from .base import *

import environ
from django.contrib.messages import constants as messages
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'URL': os.getenv('DB_SUPABASE_URL'),
        'NAME': os.getenv('DB_SUPABASE_NAME'),
        'USER': os.getenv('DB_SUPABASE_USER'),
        'PASSWORD': os.getenv('DB_SUPABASE_PASSWORD'),
        'HOST': os.getenv('DB_SUPABASE_HOST'),
        'PORT': os.getenv('DB_SUPABASE_PORT'),
    }
}

