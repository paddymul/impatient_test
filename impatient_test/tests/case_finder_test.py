

import unittest

from impatient_test.find_all_tests import *

class CaseFinderTest(unittest.TestCase):

    def test_get_test_Klasses_from_module(self):
        from dummy_test_fixture.tests import dummy_tests as dummy_test_module
        self.assertEquals(
            get_test_Klasses_from_module(dummy_test_module),
            [dummy_test_module.ExampleTests])

    def test_get_test_cases_from_Klass(self):
        from dummy_test_fixture.tests import dummy_tests as dummy_test_module
        ET = dummy_test_module.ExampleTests
        expected_test_case = getattr(ET, "test_1")
        self.assertEquals(
            set([expected_test_case]),
            set(get_test_cases_from_Klass(dummy_test_module.ExampleTests)))

    def test_get_test_module(self):
        from dummy_test_fixture.tests import dummy_tests as dummy_test_module
        DA = get_app("dummy_test_fixture") #DummmyApp

        expected_test_module = get_test_module(DA)
        from dummy_test_fixture import tests as dtf_test_module
        self.assertEquals(expected_test_module, dtf_test_module)


    def test_get_testcase_name(self):
        from dummy_test_fixture.tests import dummy_tests as dummy_test_module
        DA = get_app("dummy_test_fixture") #DummmyApp
        
        ET = dummy_test_module.ExampleTests
        test_case_fn = getattr(ET, "test_1")
        self.assertEquals(get_test_case_name(test_case_fn),
                          "test_1")
    def test_diff(self):
        from dummy_test_fixture.tests import dummy_tests as dummy_test_module
        DA = get_app("dummy_test_fixture") #DummmyApp

        self.assertNotEquals(get_test_modules_from_app(DA),
                             get_test_Klasses_from_module(DA))

    

    def test_TestDescription_eq(self):
        d1 = TestDescription("foo", "bar", "baz", "bof")
        d2 = TestDescription("foo", "bar", "baz", "bof")
        self.assertEquals(d1,d2)
        d3 = TestDescription("fo2", "bar", "baz", "bof")
        self.assertNotEquals(d2,d3)

    def test_collect_TestDescriptions(self):
        """ use dummy test module """
        from dummy_test_fixture.tests import dummy_tests as dummy_test_module
        DA = get_app("dummy_test_fixture") #DummmyApp

        ET = dummy_test_module.ExampleTests
        expected_test_case = getattr(ET, "test_1")
        expected_Klass = ET
        expected_app = "dummy_test_fixture"
        expected_invoke_string = "dummy_test_fixture.ExampleTests.test_1"

        expected_td = TestDescription(
            expected_test_case,
            expected_Klass,
            expected_app,
            expected_invoke_string)

        fixture_app_tds =get_all_TestDescriptions("dummy_test_fixture")
        #print fixture_app_tds[0]
        #print expected_td
        #pdb.set_trace()
        self.assertTrue(
            expected_td in fixture_app_tds)


if __name__ == '__main__':
    unittest.main()


