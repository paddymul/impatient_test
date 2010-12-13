import unittest

from impatient_test.distributor import collect_test
from impatient_test.find_all_tests import TestDescription
from impatient_test import distributor
from output_fixture.tests import stdout_string, stderr_string
import pdb

def make_td(invoke_string):
    return TestDescription(False, False, False, invoke_string)

class CollectionTest(unittest.TestCase):
            
    
    def test_stdout_collection(self):
        
        tr = collect_test(
            make_td("output_fixture.OutputTestKlass.test_stdout"))
        self.assertTrue(stdout_string in tr.stdout)

    def test_stderr_collection(self):
        tr = collect_test(
            make_td("output_fixture.OutputTestKlass.test_stderr"))
        self.assertTrue(stderr_string in tr.stderr)

    def test_recognize_fail(self):
        tr = collect_test(
            make_td("output_fixture.OutputTestKlass.test_mockfailure"))
        self.assertNotEquals(tr.return_code, 0)

    def test_recognize_success(self):
        tr = collect_test(
            make_td("output_fixture.OutputTestKlass.test_mocksuccess"))
        self.assertEquals(tr.return_code, 0)
        

import os
#from impatient_test.filters import 
class EnvPassTest(unittest.TestCase):

    def test_mysql_passthrough(self):

        env_mysql = os.environ.get("PPY_MYSQL", False)
        self.assertEquals(env_mysql, False)
        td = make_td("env_check.EnvCheckClass.test_mysql_env")
        td.env = {"PPY_MYSQL":"True"}
                
        [tr] = distributor.run_tests_parallel([td])
        self.assertEquals(tr.return_code, 0)
        # we want to make sure that we aren't dirtying the
        # environment, since this runs with the multiprocessing module
        # in a subprocess, that shouldn't be an issue
        env_mysql = os.environ.get("PPY_MYSQL", False)
        self.assertEquals(env_mysql, False)
        
if __name__ == '__main__':
    unittest.main()


