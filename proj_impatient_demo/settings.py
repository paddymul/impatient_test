# Django settings for proj_impatient_demo project.

# all of the default django settings have been compressed to highlight
# the differences required to us impatient_test

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = ()
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
MEDIA_ROOT = ''
MEDIA_URL = ''
ADMIN_MEDIA_PREFIX = '/media/'
SECRET_KEY = 've=un5w08o0pl^11&x$oyx7-6@(640ay-$vvvcy9y=yhh=m3-q'
TEMPLATE_LOADERS = ()
MIDDLEWARE_CLASSES = ()
ROOT_URLCONF = 'proj_impatient_demo.urls'
TEMPLATE_DIRS = ()
MANAGERS = ADMINS

DATABASE_ENGINE = ''           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ''             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

DATABASE_ENGINE = 'sqlite3'
#DATABASE_ENGINE = 'foo'

DATABASE_USER = "proj_impatient"
DATABASE_PASSWORD = "proj_impatient"


#from here down this is what is different
from impatient_test import database_determine

TEST_DB_NAME_PREFIX = "proj_impatient_demo"

DATABASE_ENGINE = database_determine.test_database_engine()
TEST_DATABASE_ENGINE = database_determine.test_database_engine()
TEST_DATABASE_NAME = database_determine.test_database_name()



import os
opj = os.path.join
# Note this is a django best practice, this will keep you from
# hardcoding paths through your application
CODE_ROOT = opj(os.path.abspath(os.path.dirname(__file__)), '..')
# required so that we can construct shell commands
PROJ_NAME = "proj_impatient_demo"

#if most of your tests require mysql, it is
#better to just label those specific tests which require sqlite3

IMPATIENT_DEFAULT_DATABASE="mysql"


INSTALLED_APPS = (
    'impatient_test',
    'db_backed_app'
)
SKIP_TESTS = ()

