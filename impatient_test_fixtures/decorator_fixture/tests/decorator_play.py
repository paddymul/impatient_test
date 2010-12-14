

import unittest
from impatient_test.decorators import *

class DecoratorExampleTests(unittest.TestCase):

    @mysql
    def test_with_mysql(self):
        self.assertTrue(1==1)
        

    @sqlite3
    def test_with_sqlite3(self):
        self.assertTrue(1==1)
        

    def test_undecorated(self):
        self.assertTrue(1==1)

    @sqlite3
    @parallel
    def test_double_decorated(self):
        self.assertTrue(1==1)
        
