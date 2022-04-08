"""
Django settings for bioecomm project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7b41cigouf)krfh@4i+7tj#+y%rp_k7xx!cq29_t(3$vf+-_lp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop.apps.ShopConfig',
    'django.contrib.humanize',
    'bootstrapform',
    'ckeditor',
    'ecomadmin.apps.EcomadminConfig',
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

ROOT_URLCONF = 'bioecomm.urls'

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

WSGI_APPLICATION = 'bioecomm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

CKEDITOR_CONFIGS = {
    'default': {
        'height':'500px',
        # tab key conversion space number
        'tabSpaces': 4,
        # Toolbar Style
        'toolbar': 'Custom',
        # Toolbar buttons
        'toolbar_Custom': [
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['Cut', 'Copy', 'Paste', 'Preview', '-', 'Print', 'SpellChecker', 'Scayt'],
            ['Smiley', 'CodeSnippet', 'SpecialChar'], 
            ['Bold', 'Italic', 'Underline', 'Strike'], 
            ['Find', 'Replace'],
            ['Subscript', 'Superscript'],
            ['SelectAll', 'RemoveFormat', 'Blockquote', 'Outdent', 'Indent'],
            ['TextColor', 'BGColor'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Anchor'],
            ['NumberedList', 'BulletedList'],
            ['Image', 'Flash', 'Table', 'HorizontalRule', 'PageBreak'],
            ['Maximize', 'About', 'pbckcode']

        ],

        # 'toolbar': (
         #   
         #   ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField'], 
         #   ,
         

        # Add Code Block Plug-ins
        'extraPlugins': ','.join(['codesnippet']),
        'codeSnippet_languages': {
            'bash': 'Bash',
            'css': 'CSS',
            'django': 'Django',
            'html': 'HTML',
            'javascript': 'JavaScript',
            'php': 'PHP',
            'python': 'Python',
        }
    }
}
# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

#DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
