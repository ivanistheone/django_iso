import os

# DJANGO
################################################################################

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True

TEMPLATE_DEBUG = DEBUG

SECRET_KEY = '_'

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'webpack',                                                         # WEBPACK
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'webpack.django_integration.WebpackFinder',                        # WEBPACK
)  

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'djangosite', 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'djangosite', 'templates'),
)

MIDDLEWARE_CLASSES = ()

ROOT_URLCONF = 'djangosite.urls'

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')



# REACT   <-->  JS host
################################################################################

from js_host.conf import settings as js_host_settings
from react.conf import settings as react_settings

js_host_settings.configure(
    USE_MANAGER=DEBUG
)

react_settings.configure(
    DEVTOOL='eval' if DEBUG else None,
)


# WEBPACK                                                           also above ^ 
################################################################################

WEBPACK = {
    'BUNDLE_ROOT': STATIC_ROOT,
    'BUNDLE_URL': STATIC_URL,
    'WATCH_CONFIG_FILES': DEBUG,
    'WATCH_SOURCE_FILES': DEBUG,
}

