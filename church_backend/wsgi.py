"""
WSGI config for New Class Royal Ministries website.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'church_backend.settings.production')

application = get_wsgi_application()
