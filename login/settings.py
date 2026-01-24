"""
Django settings for login project.
"""

import os
from pathlib import Path
from django.contrib import admin

# ----------------------------------------
# BASE_DIR
# ----------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------------------
# LOG DIRECTORY SETUP
# ----------------------------------------
LOG_DIR = BASE_DIR / 'log'
LOG_DIR.mkdir(exist_ok=True)

# ----------------------------------------
# SECURITY
# ----------------------------------------
SECRET_KEY = 'django-insecure-1ivoxc#e#rnitn7wyvmfbxd-15j=*)a1y9z8of*qo*((qx8h+o'
DEBUG = False
ALLOWED_HOSTS = ["*"]

# ----------------------------------------
# APPLICATIONS
# ----------------------------------------
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'myapp',
    'myapp1',
    'network',
]

# Jazzmin Admin Theme
JAZZMIN_SETTINGS = {
    "site_title": "My Admin Panel",
    "site_header": "My Custom Admin",
    "site_brand": "Admin Dashboard",
    "welcome_sign": "Welcome to My Admin!",
    "copyright": "© 2024 My Company",
    # "site_logo": "your_app/logo.png",  
    # "search_model": "your_app.Contact",  
}

# ----------------------------------------
# MIDDLEWARE
# ----------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'login.middleware.restrict_admin.BlockAdminForNonSuperusers',
]

ROOT_URLCONF = 'login.urls'

# ----------------------------------------
# TEMPLATES
# ----------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "Templates"],
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

WSGI_APPLICATION = 'login.wsgi.application'

# ----------------------------------------
# DATABASE
# ----------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ----------------------------------------
# PASSWORD VALIDATION
# ----------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ----------------------------------------
# INTERNATIONALIZATION
# ----------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ----------------------------------------
# STATIC & MEDIA FILES
# ----------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# ----------------------------------------
# LOGGING
# ----------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': LOG_DIR / 'admin_access.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}

# ----------------------------------------
# CUSTOM ADMIN SITE (Superuser Only)
# ----------------------------------------
class SuperuserOnlyAdminSite(admin.AdminSite):
    def has_permission(self, request):
        return request.user.is_active and request.user.is_superuser

admin.site = SuperuserOnlyAdminSite()
