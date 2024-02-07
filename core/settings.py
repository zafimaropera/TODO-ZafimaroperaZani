"""
Paramètres Django pour le projet core.
Généré par 'django-admin startproject' en utilisant Django 4.1.3.
Pour plus d'informations sur ce fichier, voir
https://docs.djangoproject.com/en/4.1/topics/settings/
Pour la liste complète des paramètres et de leurs valeurs, voir
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Construire des chemins à l'intérieur du projet de cette manière : BASE_DIR / 'sous-répertoire'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')


# Paramètres de développement rapide - inadaptés pour la production
# Voir https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# AVERTISSEMENT DE SÉCURITÉ : gardez la clé secrète utilisée en production secrète !
SECRET_KEY = 'django-insecure-99#a9@gyvigirim+v6_lsj*u@35+7tv%96#@+nyr0_@+^m%ldc'

# AVERTISSEMENT DE SÉCURITÉ : ne pas exécuter avec le mode de débogage activé en production !
DEBUG = True

ALLOWED_HOSTS = []


# Définition des applications

INSTALLED_APPS = [  
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     
    'myapp', # Mon Application
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages', 
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Base de données
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), 
    }
}



# Validation des mots de passe
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalisation
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'fr-FR'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True 
USE_TZ = True

# Fichiers statiques (CSS, JavaScript, images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Type de champ de clé primaire par défaut
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 
