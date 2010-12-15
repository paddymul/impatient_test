"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from impatient_test.decorators import mysql, sqlite3

class SimpleTest(TestCase):

    @sqlite3
    def test_sqlite3_decorator(self):
        """
        this demonstrates the sqlite3 decorator
        
        """
        from django.conf import settings
        self.failUnlessEqual(1 + 1, 2)
        self.assertEquals(
            settings.TEST_DATABASE_ENGINE,
            "sqlite3")

    def test_undecorated_db(self):
        """
        note that because settings.IMPATIENT_DEFAULT_DATABASE="mysql"
        this test will get a mysql database 
        
        """
        from django.conf import settings
        self.assertEquals(
            settings.TEST_DATABASE_ENGINE,
            "mysql")
        

    @mysql
    def test_mysql_decorator(self):
        """
        
        """
        from django.conf import settings
        self.assertEquals(
            settings.TEST_DATABASE_ENGINE,
            "mysql")
        
