




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
def get_tests(app_module):
    try:
        app_path = app_module.__name__.split('.')[:-1]
        test_module = __import__('.'.join(app_path + [TEST_MODULE]), {}, {}, TEST_MODULE)
    except ImportError, e:
        # Couldn't import tests.py. Was it due to a missing file, or
        # due to an import error in a tests.py that actually exists?
        import os.path
        from imp import find_module
        try:
            mod = find_module(TEST_MODULE, [os.path.dirname(app_module.__file__)])
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

def get_test_classes_from_module(module):
    """Return a suite of all tests cases contained in the given module"""
    testcases = []
    for name in dir(module):
        obj = getattr(module, name)
        if (isinstance(obj, (type, types.ClassType)) and
            issubclass(obj, TestCase)):
            testcases.append(obj)
            #tests.append(self.loadTestsFromTestCase(obj))
    #return self.suiteClass(tests)
    return testcases

def get_testcases(app_module):
    app_name = app_module.__name__.split(".")[-2]
    test_module = get_tests(app_module)
    test_names = []
    
    if test_module:
        tl = unittest.TestLoader()
        print test_module
        app_module.__name__.split(".")[-1]
        for testclass in get_test_classes_from_module(test_module):
            test_case_names = tl.getTestCaseNames(testclass)
            for test_case_name in test_case_names:
                test_names.append(".".join(
                    [app_name , testclass.__name__, test_case_name]))
    return test_names

import os
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
from os.path import join as opj
import subprocess
import tempfile
import datetime
import multiprocessing 


        
if __name__== "__main__":
    print get_individual_test_names(get_filtered_apps())

