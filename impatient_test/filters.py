from django.test import TestCase as djTestCase
from django.conf import settings


def filter_by_case_fn_attr(prop, tds):
    ret_tds = []
    for td in tds:
        if getattr(td.case_fn, prop, False):
            ret_tds.append(td)
    return ret_tds

def make_case_fn_attr_filter(prop):
    def constructed_p(td):
        return getattr(td.case_fn, prop, False)
    return constructed_p


def complement(f):
    def new_f(*args, **kwargs):
        return not f(*args, **kwargs)
    return new_f

def requires_database(td):
    return issubclass(td.Klass, djTestCase)

requires_mysql = make_case_fn_attr_filter("mysql")
requires_sqlite = make_case_fn_attr_filter("sqlite")

import pdb

def mysql_env(td, count):
    td.env['PPY_MYSQL']="True"
    td.env['PPY_MYSQL_NAME']="%s_%d" % (settings.TEST_DB_NAME_PREFIX, count)

def sqlite_env(td, count):
    td.env['PPY_SQLITE']="True"
    td.env['PPY_SQLITE_NAME']=":memory:"
    


def construct_envs(tds):

    
    
    no_db = filter(complement(requires_database), tds)
    for td in no_db:
        sqlite_env(td, 0)

    
    
    db_reqs = filter(requires_database, tds)

    mysql_count = 0

    def default_env(td):
        if settings.IMPATIENT_DEFAULT_DATABASE == "mysql":
            mysql_env(td, mysql_count)
        else:
            sqlite_env(td, mysql_count)
    
    for td in db_reqs:
        #pdb.set_trace()
        if requires_mysql(td):
            mysql_env(td, mysql_count)
        elif requires_sqlite(td):
            sqlite_env(td, mysql_count)
        else:
    
            default_env(td)
        mysql_count += 1
        
    mysql_reqs = filter(requires_mysql, db_reqs)
    sqlite_reqs = filter(complement(requires_mysql), db_reqs)

    mysql_dbs = len(mysql_reqs)
    print "%d separate mysql databases required "

    final_tds = []

    final_tds.extend(db_reqs)
    #final_tds.extend(mysql_reqs)
    #final_tds.extend(sqlite_reqs)
    final_tds.extend(no_db)

    return tds
        
    
    
def culled_apps():
    culled = []
    for app in settings.INSTALLED_APPS:
        if app in settings.SKIP_TESTS:
            continue
        culled.append(app)
    return culled

#print "calling culled_apps", culled_apps()
