
def mysql(fn):
    """ used to denote that a testcase or testKlass requires mysql """
    fn.mysql=True
    return fn

def sqlite3(fn):
    """ used to denote that a testcase or testKlass requires sqlite3 """
    fn.sqlite3=True
    return fn

def parallel(fn):
    fn.parallel=True
    return fn
