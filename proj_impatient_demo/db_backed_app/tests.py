"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from impatient_test.decorators import mysql

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        
        """
        from django.conf import settings
        self.failUnlessEqual(1 + 1, 2)
        self.assertEquals(
            settings.TEST_DATABASE_ENGINE,
            "sqlite3")
        

    @mysql
    def test_basic_addition_with_mysql(self):
        """
        Tests that 1 + 1 always equals 2.
        
        """
        self.failUnlessEqual(1 + 1, 2)
        from django.conf import settings
        self.assertEquals(
            settings.TEST_DATABASE_ENGINE,
            "mysql")
        
