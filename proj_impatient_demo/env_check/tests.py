"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
import os

class EnvCheckClass(TestCase):
    def test_mysql_env(self):

        env_mysql = os.environ.get("PPY_MYSQL", False)
        print "env mysql" 
        self.assertEquals(env_mysql, "True")
        
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

