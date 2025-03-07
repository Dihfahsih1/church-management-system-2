 

from pathlib import Path
 
BASE_DIR = Path(__file__).resolve().parent.parent
 
SECRET_KEY = 'django-insecure-%835wgu)7x$bx7bzba1(ve5tczw*eunk@pabry8nwf45uj)o+q'
 
DEBUG = True

ALLOWED_HOSTS = []
 

INSTALLED_APPS = [
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'frontend',
    'rest_framework',
]

AUTH_USER_MODEL = 'accounts.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',  # Enables session-based auth
        'rest_framework.authentication.TokenAuthentication',  # Enables token-based auth (if needed)
    ),
}
MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    
]

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8000",  
]

ROOT_URLCONF = 'church_management_system.urls'

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



WSGI_APPLICATION = 'church_management_system.wsgi.application'
 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'finance',
        'USER': 'root', 
        'PASSWORD': '', 
        'HOST': '127.0.0.1', 
        'PORT': '3306',
    }
}


 

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default backend
]
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True

USE_TZ = True

 

# URL to use when referring to static files
STATIC_URL = '/static/'

# Directory where static files are stored, typically under your project directory
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # for local static files
]

# Directory where collected static files will be stored for production (useful for `collectstatic` command)
STATIC_ROOT = BASE_DIR / 'staticfiles'  # For production, after running `python manage.py collectstatic`

# URL to use when referring to media files (uploads)
MEDIA_URL = '/media/'

# Directory where media files are stored (uploads from users, for example)
MEDIA_ROOT = BASE_DIR / 'media'  # Path where uploaded files will be stored

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
