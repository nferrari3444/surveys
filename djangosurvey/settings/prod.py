from .base import *

ACCOUNT_DEFAULT_HTTP_PROTOCOL='https'

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

