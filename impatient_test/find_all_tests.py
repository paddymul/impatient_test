import unittest
from django.conf import settings
from django.db.models import get_app, get_apps
from django.test import _doctest as doctest
from django.test.utils import setup_test_environment, teardown_test_environment
from django.test.testcases import OutputChecker, DocTestRunner, TestCase

# The module name for tests outside models.py
TEST_MODULE = 'tests'

import pdb
import types

"""
Definitions

* app
is an application as defined by django, will be found in settings.INSTALLED_APPS
* test_module
the module of an app that contains testKlasses
for impatient_test the test module is impatient_test.tests, in file
impatient_tests/tests/__init__.py
* test_Klass
a class that extends unittest.TestCase
* test_case
a member function of a test_Klass



"""

        


###### Functions that operate on apps

def get_filtered_apps():
    """ this does basically what django test extensions does """
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

def get_app_name_from_test_Klass(testKlass):
    """for a test module such as impatient_test.tests.ExampleTests
    return impatient_test
    """
    return testKlass.__name__.split(".")[-2]

def get_test_modules_from_app(app_module):

    test_module = get_test_module(app_module)
    test_Klasses = []
    if test_module:
        tl = unittest.TestLoader()
        for test_Klass in get_test_Klasses_from_module(test_module):
            test_Klasses.append(test_Klass)
    return test_Klasses

###### functions that operate on testModules

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
    
###### functions that operate on testKlasses

def get_test_cases_from_Klass(testCaseKlass):
    """ returns the actual functions """
    testMethodPrefix = "test"
    def isTestMethod(attrname,
                     testCaseKlass=testCaseKlass,
                     prefix=testMethodPrefix):
        prefix_pred = attrname.startswith(prefix)
        callable_pred = hasattr(getattr(testCaseKlass, attrname), '__call__')
        return prefix_pred  and callable_pred
    testFnNames = filter(isTestMethod, dir(testCaseKlass))

    test_cases = []
    for testFnName in testFnNames:
        test_cases.append(getattr(testCaseKlass, testFnName))
    return test_cases

def get_test_case_name(testCase):
    """ given a testCase, returns the name of that testCase """
    return testCase.__name__

class TestDescription(object):
    """ A description of a single test case

    """
    def __init__(self, case_fn, Klass, app, invoke_string, env={}):
        self.case_fn, self.Klass = case_fn, Klass
        self.app, self.invoke_string =  app, invoke_string
        self.env = {}

    def __eq__(self, other):
        """ primarily used for testing impatient_test's functionality
        """
        
        for k in ["case_fn", "Klass", "app", "invoke_string"]:
            if not getattr(self, k) == getattr(other, k):
                return False
        return True

    def __str__(self):
        return "TestDescription(%r, %r, %r, %r)" % (self.case_fn, self.Klass, self.app, self.invoke_string)

    def __repr__(self):
        return self.__str__()

    def __getstate__(self):
        """ functions and classes aren't pickleable, so we exclude them """
        state = self.__dict__.copy()
        del state['Klass']
        del state['case_fn']
        return state


    def __setstate__(self, state):

        self.__dict__.update(state)
        self.__dict__['Klass']=False
        self.__dict__['case_fn']=False

def get_all_TestDescriptions(app_name=None):
    try:
        app = get_app(app_name.split(".")[-1])
        test_module = get_test_module(app)
        tds = []  # TestDescriptions
        for testKlass in get_test_Klasses_from_module(test_module):
            for tc in get_test_cases_from_Klass(testKlass):
                tds.append(
                    TestDescription(case_fn = tc,
                                    Klass = testKlass,
                                    app = app_name,
                                    invoke_string = create_invoke_string(
                                                   app_name, testKlass, tc)))
        return tds
    except:
        return []


def create_invoke_string(app_name, testKlass, case_fn):
    normalized_app_name = app_name.split(".")[-1]
    return ".".join(
        [normalized_app_name , testKlass.__name__, case_fn.__name__])

###### Monolithic old functions 
def get_testcases(app_module):
    app_name = get_app_name(app_module)
    test_module = get_test_module(app_module)
    test_names = []
    
    if test_module:
        tl = unittest.TestLoader()
        print test_module
        for testKlass in get_test_Klasses_from_module(test_module):
            pdb.set_trace()
            test_case_names = tl.getTestCaseNames(testKlass)
            for test_case_name in test_case_names:
                test_names.append(".".join(
                    [app_name , testKlass.__name__, test_case_name]))
    return test_names

def get_individual_test_names(test_labels):
    test_list = []

    if hasattr(settings, 'SKIP_TESTS'):
        #for app in settings.SKIP_TESTS
        pass
    for app in test_labels:
        test_list.extend(get_testcases(app))
    return test_list


        
if __name__== "__main__":
    pdb.set_trace()
    ab = get_filtered_apps()
    ac = ab[0]

    ka = get_test_Klasses_from_module(ac)
    kb = ka[0]

    tca = get_test_cases_from_Klass(kb)
    
    #ab= get_test_cases_from_Klass(get_test_Klasses_from_module(get_filtered_apps()[0])[3])
    #ab= get_test_cases_from_Klass(get_testKlasses(get_app("impatient_test"))[0])
    print ab
    lyt1 = ab[0]
    pdb.set_trace()

    print ab
    #print get_individual_test_names(get_filtered_apps())

