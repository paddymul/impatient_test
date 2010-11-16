




import unittest
from django.conf import settings
from django.db.models import get_app, get_apps
from django.test import _doctest as doctest
from django.test.utils import setup_test_environment, teardown_test_environment
from django.test.testcases import OutputChecker, DocTestRunner, TestCase


# The module name for tests outside models.py
TEST_MODULE = 'tests'

doctestOutputChecker = OutputChecker()
import pdb
import types

def get_test_module(app_module):
    try:
        app_path = app_module.__name__.split('.')[:-1]
        mod_name = '.'.join(app_path + [TEST_MODULE])
        test_module = __import__(mod_name, {}, {}, TEST_MODULE)
    except ImportError, e:
        # Couldn't import tests.py. Was it due to a missing file, or
        # due to an import error in a tests.py that actually exists?
        import os.path
        from imp import find_module
        try:
            mod_file = [os.path.dirname(app_module.__file__)]
            mod = find_module(TEST_MODULE, mod_file)
        except ImportError:
            # 'tests' module doesn't exist. Move on.
            test_module = None
        else:
            # The module exists, so there must be an import error in the
            # test module itself. We don't need the module; so if the
            # module was a single file module (i.e., tests.py), close the file
            # handle returned by find_module. Otherwise, the test module
            # is a directory, and there is nothing to close.
            if mod[0]:
                mod[0].close()
            raise
    return test_module

def get_test_Klasses_from_module(module):
    """Return a suite of all tests cases contained in the given module"""
    testcases = []
    for name in dir(module):
        obj = getattr(module, name)
        if (isinstance(obj, (type, types.ClassType)) and
            issubclass(obj, unittest.TestCase)):
            testcases.append(obj)
            #tests.append(self.loadTestsFromTestCase(obj))
    #return self.suiteClass(tests)
    return testcases

def get_testcases(app_module):
    app_name = app_module.__name__.split(".")[-2]
    test_module = get_test_module(app_module)
    test_names = []
    
    if test_module:
        tl = unittest.TestLoader()
        print test_module
        app_module.__name__.split(".")[-1]
        for testKlass in get_test_Klasses_from_module(test_module):
            pdb.set_trace()
            test_case_names = tl.getTestCaseNames(testKlass)
            for test_case_name in test_case_names:
                test_names.append(".".join(
                    [app_name , testKlass.__name__, test_case_name]))
    return test_names

def get_testKlasses(app_module):
    app_name = app_module.__name__.split(".")[-2]

    test_module = get_test_module(app_module)

    test_Klasses = []
    if test_module:
        tl = unittest.TestLoader()
        print test_module
        app_module.__name__.split(".")[-1]
        for test_Klass in get_test_Klasses_from_module(test_module):
            test_Klasses.append(test_Klass)

    return test_Klasses

def get_test_modules_from_app(app):
    app_name = app_module.__name__.split(".")[-2]
    test_module = get_test_module(app_module)
    if test_module:
        tl = unittest.TestLoader()
        app_module.__name__.split(".")[-1]
        for test_Klass in get_test_Klasses_from_module(test_module):
            test_Klasses.append(test_Klass)

    return test_Klasses
    

def getTestCaseNames(self, testCaseKlass):
    """Return a sorted sequence of method names found within testCaseKlass
    """
    testMethodPrefix = "test"
    def isTestMethod(attrname, testCaseKlass=testCaseKlass, prefix=testMethodPrefix):
        return attrname.startswith(prefix) and hasattr(getattr(testCaseKlass, attrname), '__call__')
    testFnNames = filter(isTestMethod, dir(testCaseKlass))
    if self.sortTestMethodsUsing:
        testFnNames.sort(key=_CmpToKey(self.sortTestMethodsUsing))
    return testFnNames


def get_test_cases_from_Klass(testCaseKlass):
    testMethodPrefix = "test"
    def isTestMethod(attrname, testCaseKlass=testCaseKlass, prefix=testMethodPrefix):
        return attrname.startswith(prefix) and hasattr(getattr(testCaseKlass, attrname), '__call__')
    testFnNames = filter(isTestMethod, dir(testCaseKlass))

    test_cases = []
    for testFnName in testFnNames:
        test_cases.append(getattr(testCaseKlass, testFnName))
    return test_cases



def get_individual_test_names(test_labels):
    test_list = []

    if hasattr(settings, 'SKIP_TESTS'):
        #for app in settings.SKIP_TESTS
        pass
    for app in test_labels:
        test_list.extend(get_testcases(app))
    return test_list

def get_filtered_apps():
    test_labels=[]
    if hasattr(settings, 'SKIP_TESTS'):
        if not test_labels:
            test_labels = list()
            for app in get_apps():
                test_labels.append(app.__name__.split('.')[-2])
        for app in settings.SKIP_TESTS:
            try:
                test_labels = list(test_labels)
                test_labels.remove(app)
            except ValueError:
                pass
        return map(get_app, test_labels)
    else:
        return get_apps()
        
if __name__== "__main__":
    ab= get_test_cases_from_Klass(get_testKlasses(get_filtered_apps()[0])[3])
    ab= get_test_cases_from_Klass(get_testKlasses(get_app("impatient_test"))[0])
    print ab
    lyt1 = ab[0]
    pdb.set_trace()

    print ab
    #print get_individual_test_names(get_filtered_apps())

