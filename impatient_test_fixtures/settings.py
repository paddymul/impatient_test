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


#from here down this is what is different
from impatient_test import database_determine

TEST_DB_NAME_PREFIX = "impatient_test_fixtures"

TEST_DATABASE_ENGINE = database_determine.test_database_engine()
TEST_DATABASE_NAME = database_determine.test_database_name()



import os
opj = os.path.join
# Note this is a django best practice, this will keep you from
# hardcoding paths through your application
CODE_ROOT = opj(os.path.abspath(os.path.dirname(__file__)), '..')
# required so that we can construct shell commands
PROJ_NAME = "impatient_test_fixtures"

INSTALLED_APPS = (
    'impatient_test',
    'decorator_fixture',
    'env_check',
    'db_switch',
    'output_fixture',
    'dummy_test_fixture', 
)
SKIP_TESTS = ()
