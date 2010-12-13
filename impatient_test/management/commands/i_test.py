import sys
from optparse import make_option

from django.core import management
from django.conf import settings
from django.db.models import get_app, get_apps
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *test_labels, **options):
        

        from impatient_test.find_all_tests import get_all_TestDescriptions
        from impatient_test.distributor import run_tests_parallel, summarize_results
        from django.conf import settings



        all_tds = []
        for app in settings.INSTALLED_APPS:
            all_tds.extend(get_all_TestDescriptions(app))


        summarize_results(run_tests_parallel(all_tds))

