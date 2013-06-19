# Django settings for myproject project.
import os
import sys
from socket import gethostname

#Flag for changing setting if project is running on dev or prd server
if 'myhost' in gethostname():
	in_production = True
else:
	in_production = False
	
if in_production:
	DEBUG = False
	TEMPLATE_DEBUG = False
else:
	DEBUG = True
	TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = os.path.dirname(__file__)

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'myproject.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
)

#Installed Apps
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'apps.tagging',
    'south',
    'sorl.thumbnail',
    'disqus',
    'apps.blog',
    'apps.links',
    'apps.images',
    'apps.video',
    'google_analytics',
    'pygments',
    'tinymce',
)

DISQUS_API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
DISQUS_WEBSITE_SHORTNAME = 'myproject'
GOOGLE_ANALYTICS_MODEL = True

if in_production:
	DATABASES = {
		'default': {
		    'ENGINE': 'django.db.backends.mysql', 
		    'NAME': 'myproject',                      # Or path to database file if using sqlite3.
		    'USER': 'user',                      # Not used with sqlite3.
		    'PASSWORD': 'password',                  # Not used with sqlite3.
		    'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
		    'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
		}
	}
else:
	DATABASES = {
		'default': {
		    'ENGINE': 'django.db.backends.mysql', 
		    'NAME': 'myproject',                      # Or path to database file if using sqlite3.
		    'USER': 'user',                      # Not used with sqlite3.
		    'PASSWORD': 'password',                  # Not used with sqlite3.
		    'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
		    'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
		}
	}


# Static data and media files
if in_production:
	MEDIA_URL = 'http://myhost.com/static/media/'
	ADMIN_MEDIA_PREFIX = 'http://myhost.com/static/admin/'
	STATIC_URL = 'http://myhost.com/static/'
	MEDIA_ROOT = '/home/willoem/webapps/static/media'
	STATIC_ROOT = '/home/willoem/webapps/static'

else:
	MEDIA_URL = '/static/media/'
	ADMIN_MEDIA_PREFIX = '/static/admin/'
	STATIC_URL = '/static/'
	STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, 'static'),)
	MEDIA_ROOT = os.path.join('/home/willoem/Code/Python/Django/myproject/static/media')
	STATIC_ROOT = '/static/'



