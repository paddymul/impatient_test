

import unittest

from impatient_test.find_all_tests import *
from impatient_test.filters import filter_by_case_fn_attr
class CaseFinderTest(unittest.TestCase):
            
    
    def test_find_test_by_decorator(self):
        tds = get_all_TestDescriptions("decorator_fixture")
        filtered_tds = filter_by_case_fn_attr("mysql", tds)
        print "*"*80
        print "filtered_tds"
        print "*"*80
        print filtered_tds
        print "*"*80
        print "filtered_tds"
        print "*"*80




if __name__ == '__main__':
    unittest.main()


