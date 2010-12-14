import sys
from optparse import make_option

from django.core import management
from django.conf import settings
from django.db.models import get_app, get_apps
from django.core.management.base import BaseCommand


MYSQL_CREATE_COMMMAND = """create schema %%s;
grant all on  %%s.* to '%s'@'localhost';""" % (settings.DATABASE_USER)
class Command(BaseCommand):
    help = """This command gives the sql necessary to create every database needed by the test, since their could be many test_databases, it is best to script this.  you can pipe this to mysql to a mysql client with the proper permissions , and all of your databases will be created for you """
    def handle(self, *test_labels, **options):
        

        from impatient_test.find_all_tests import get_all_TestDescriptions
        from impatient_test.filters import requires_database, requires_mysql, complement
        from impatient_test.filters import culled_apps
        
        from django.conf import settings

        all_tds = []
        #import pdb
        #pdb.set_trace()
        for app in culled_apps():
            all_tds.extend(get_all_TestDescriptions(app))
        #print culled_apps
        #print all_tds
        db_reqs = filter(requires_database, all_tds)
        mysql_reqs = filter(requires_mysql, db_reqs)
        #import pdb
        #pdb.set_trace()
        mysql_count=0

        for db in mysql_reqs:
            db_name = "%s_%d" % (settings.TEST_DB_NAME_PREFIX, mysql_count)
            print MYSQL_CREATE_COMMMAND % (db_name, db_name)
            mysql_count += 1

