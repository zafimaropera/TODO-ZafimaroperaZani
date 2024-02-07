"""
Configuration ASGI pour le projet core.

Il expose l'appelable ASGI en tant que variable de niveau module nommée ``application``.

Pour plus d'informations sur ce fichier, consultez
https://docs.djangoproject.com/fr/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()
