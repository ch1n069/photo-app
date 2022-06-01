"""
WSGI config for photolab project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application


os.environ['DJANGO_SETTINGS_MODULE'] = 'photolab.settings'
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','photolab.settings')

application = get_wsgi_application()

