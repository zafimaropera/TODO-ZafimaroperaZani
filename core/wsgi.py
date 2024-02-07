"""
Configuration WSGI pour le projet core.

Il expose l'appelable WSGI en tant que variable de niveau module nommée ``application``.

Pour plus d'informations sur ce fichier, consultez
https://docs.djangoproject.com/fr/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()
