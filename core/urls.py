"""Configuration des URL du projet core

La liste `urlpatterns` routage des URL vers des vues. Pour plus d'informations, veuillez consulter :
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Exemples :
Vues basées sur des fonctions
    1. Ajouter une importation :  from my_app import views
    2. Ajouter une URL à urlpatterns :  path('', views.home, name='home')
Vues basées sur des classes
    1. Ajouter une importation :  from other_app.views import Home
    2. Ajouter une URL à urlpatterns :  path('', Home.as_view(), name='home')
Inclusion d'un autre fichier de configuration d'URL
    1. Importer la fonction include() : from django.urls import include, path
    2. Ajouter une URL à urlpatterns :  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Ajouter cela
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Ajouter cela
