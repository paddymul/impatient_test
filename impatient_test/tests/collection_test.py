import unittest

from impatient_test.distributor import collect_test
from output_fixture.tests import stdout_string, stderr_string
import pdb

class CollectionTest(unittest.TestCase):
            
    
    def test_stdout_collection(self):
        tr = collect_test("output_fixture.OutputTestKlass.test_stdout")
        #print stdout_string
        #print tr.stdout
        #pdb.set_trace()
        self.assertTrue(stdout_string in tr.stdout)

    def test_stderr_collection(self):
        tr = collect_test("output_fixture.OutputTestKlass.test_stderr")
        #print stdout_string
        #print tr.stdout
        #pdb.set_trace()
        self.assertTrue(stderr_string in tr.stderr)


        #print tr.stdout

        
if __name__ == '__main__':
    unittest.main()


