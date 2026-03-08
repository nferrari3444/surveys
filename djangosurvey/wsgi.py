"""
WSGI config for djangosurvey project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from djangosurvey.settings import base
from django.core.wsgi import get_wsgi_application

if base.DEBUG == True:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangosurvey.settings.dev')
    
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangosurvey.settings.prod')



application = get_wsgi_application()

app = application
