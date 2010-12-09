

import unittest

from impatient_test.find_all_tests import *
from impatient_test.tests import dummy_tests as dummy_test_module
ET = dummy_test_module.ExampleTests
IA = get_app("impatient_test")
class CaseFinderTest(unittest.TestCase):

    def test_get_test_Klasses_from_module(self):
        
        self.assertEquals(
            get_test_Klasses_from_module(dummy_test_module),
            [dummy_test_module.ExampleTests])

    def test_get_test_cases_from_Klass(self):
        expected_test_case = getattr(ET, "test_1")
        self.assertEquals(
            set([expected_test_case]),
            set(get_test_cases_from_Klass(dummy_test_module.ExampleTests)))

    def test_get_test_module(self):
        expected_test_module = get_test_module(IA)
        from impatient_test import tests as impatient_test_test_module
        self.assertEquals(expected_test_module,impatient_test_test_module)


    def test_get_testcase_name(self):
        test_case_fn = getattr(ET, "test_1")
        self.assertEquals(get_test_case_name(test_case_fn),
                          "test_1")
    def test_diff(self):
        self.assertNotEquals(get_test_modules_from_app(IA),
                             get_test_Klasses_from_module(IA))

    
    '''
    def test_diff(self):
        testModule =get_test_module(get_app("impatient_test"))
    
        self.assertNotEquals(
            get_testKlasses(testModule),
            get_test_Klasses_from_module(testModule))

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


