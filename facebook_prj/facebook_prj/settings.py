"""
Django settings for facebook_prj project.

Generated by 'django-admin startproject' using Django 2.2.28.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'er@5je=ip07w+gf43bz+&_v4*7bbnct@2pk__j!9ps_^z*j9uo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #Custom apps
    'userauths',
    'core',
    'addon',


    # Third party apps

    'crispy_forms',
    'taggit',
    'import_export',
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

ROOT_URLCONF = 'facebook_prj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processor.my_context_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'facebook_prj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEBUG = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

AUTH_USER_MODEL = "userauths.User"

LOGIN_REDIRECT_URL = 'core:feed'
LOGOUT_REDIRECT_URL = 'userauths:sign-up'
LOGIN_URL = 'userauths:sign-up'



JAZZMIN_SETTINGS= {
    # title of the window (Will default to current_admin_site.site_title)
    "site_title": "Facebook Clone",
    # Title on the login screen (19 chars max) (will default to current_admin_site.site_header)
    "site_header": "Facebook",
    # Title on the brand (19 chars max) (will default to current_admin_site.site_header)
    "site_brand": "Connecting the world together...",
    # Relative path to logo for your site, used for brand on top left (must be present in static files)
    "site_logo": "vendor/adminlte/img/AdminLTELogo.png",
    # Relative path to logo for your site, used for login logo (must be present in static files. Defaults to site_logo)
    "login_logo": None,
    # Logo to use for login form in dark themes (must be present in static files. Defaults to login_logo)
    "login_logo_dark": None,
    # CSS classes that are applied to the logo
    "site_logo_classes": "img-circle",
    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,
    # Welcome text on the login screen
    "welcome_sign": "Welcome to Facebook Admin , Login now",
    # Copyright on the footer
    "copyright": "",
    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": None,
    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    # Links to put along the nav bar
    "topmenu_links": [],
    #############
    # User Menu #
    #############
    # Additional links to include in the user menu on the top right ('app' url type is not allowed)
    "usermenu_links": [],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": True,
    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],
    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
    # List of apps to base side menu ordering off of
    "order_with_respect_to": ["core", "addon", "userauths"],
    # Custom links to append to side menu app groups, keyed on app name
    "custom_links": {},
    # Custom icons for side menu apps/models See the link below
    # https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,
    # 5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,
    # 5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {"auth": "fas fa-users-cog", "auth.user": "fas fa-user", "auth.Group": "fas fa-users"},
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    #################
    # Related Modal #
    #################
    # Activate Bootstrap modal
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {},
    # Add a language dropdown into the admin
    "language_chooser": False,
}

#######################################
# Currently available UI tweaks       #
# Use the UI builder to generate this #
#######################################

JAZZMIN_UI_TWEAKS = {
    # Small text on the top navbar
    "navbar_small_text": False,
    # Small text on the footer
    "footer_small_text": False,
    # Small text everywhere
    "body_small_text": True,
    # Small text on the brand/logo
    "brand_small_text": False,
    # brand/logo background colour
    "brand_colour": False,
    # Link colour
    "accent": "accent-primary",
    # topmenu colour
    "navbar": "navbar-white navbar-light",
    # topmenu border
    "no_navbar_border": False,
    # Make the top navbar sticky, keeping it in view as you scroll
    "navbar_fixed": False,
    # Whether to constrain the page to a box (leaving big margins at the side)
    "layout_boxed": False,
    # Make the footer sticky, keeping it in view all the time
    "footer_fixed": False,
    # Make the sidebar sticky, keeping it in view as you scroll
    "sidebar_fixed": False,
    # sidemenu colour
    "sidebar": "sidebar-dark-primary",
    # sidemenu small text
    "sidebar_nav_small_text": False,
    # Disable expanding on hover of collapsed sidebar
    "sidebar_disable_expand": False,
    # Indent child menu items on sidebar
    "sidebar_nav_child_indent": False,
    # Use a compact sidebar
    "sidebar_nav_compact_style": False,
    # Use the AdminLTE2 style sidebar
    "sidebar_nav_legacy_style": False,
    # Use a flat style sidebar
    "sidebar_nav_flat_style": False,
    # Bootstrap theme to use (default, or from bootswatch, see THEMES below)
    "theme": "default",
    # Theme to use instead if the user has opted for dark mode (e.g darkly/cyborg/slate/solar/superhero)
    "dark_mode_theme": None,
    # The classes/styles to use with buttons
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}
