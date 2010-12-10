

import unittest

from impatient_test.find_all_tests import *
from impatient_test.filters import filter_by_case_fn_attr
from decorator_fixture.tests import DecoratorExampleTests

class FiltersTest(unittest.TestCase):
            
    
    def test_find_test_by_decorator(self):
        tds = get_all_TestDescriptions("decorator_fixture")
        filtered_tds = filter_by_case_fn_attr("mysql", tds)
        self.assertEquals(len(filtered_tds), 1)
        
        actual_td = filtered_tds[0]
        self.assertEquals(actual_td.Klass, DecoratorExampleTests)
        self.assertEquals(actual_td.case_fn,
                          DecoratorExampleTests.test_with_mysql)

    def test_double(self):
        """ we wanted to see if we could double stack decorators, you
        can, and we still filter properly
        """
        
        tds = get_all_TestDescriptions("decorator_fixture")
        filtered_tds = filter_by_case_fn_attr("sqlite3", tds)
        print filtered_tds
        self.assertEquals(len(filtered_tds), 2)

        filtered_tds = filter_by_case_fn_attr("parallel", tds)
        print filtered_tds
        self.assertEquals(len(filtered_tds), 1)


if __name__ == '__main__':
    unittest.main()


