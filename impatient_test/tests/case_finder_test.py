

import unittest

from impatient_test.find_all_tests import *
from impatient_test.tests import dummy_tests as dummy_test_module
class CaseFinderTest(unittest.TestCase):

    def test_get_test_Klasses_from_module(self):
        self.assertEquals(
            get_test_Klasses_from_module(dummy_test_module),
            [dummy_test_module.ExampleTests])

    def test_get_test_cases_from_Klass(self):
        ET = dummy_test_module.ExampleTests
        #pdb.set_trace()
        self.assertEquals(
            set([getattr(ET, "test_1")]),
            set(get_test_cases_from_Klass(dummy_test_module.ExampleTests)))
    def test_get_test_module(self):
        app = get_app("impatient_test")
        ab = get_test_module(app)
        from impatient_test import tests as impatient_test_test_module
        self.assertEquals(ab,impatient_test_test_module)

    '''
    def test_1(self):
        app =  get_app("impatient_test")

        classes =  get_testclasses(app)
        ab = get_test_cases_from_class(classes)
        print ab
        #pdb.set_trace()
        print ab
    '''
           
            
   



if __name__ == '__main__':
    unittest.main()


