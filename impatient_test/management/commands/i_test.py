import sys
from optparse import make_option

from django.core import management
from django.conf import settings
from django.db.models import get_app, get_apps
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    option_list =BaseCommand.option_list +  (
        make_option(
            '--max_tests', action='store',
            dest='max_tests', #default=False,
            help='Maximum number of tests to run, (mostly for debugging)'),
        make_option(
            '--show_all_output', action='store_true',
            dest='show_all_output', default=False,
            help='show output even from passing tests'),
    )


    def handle(self, *test_labels, **options):
        

        from impatient_test.find_all_tests import get_all_TestDescriptions
        from impatient_test.distributor import run_tests_parallel, summarize_results
        from impatient_test.filters import culled_apps, construct_envs
        from django.conf import settings
        import pdb
        print options
        #

        all_tds = []
        for app in culled_apps():
            all_tds.extend(get_all_TestDescriptions(app))
        #1/0



        env_tds = construct_envs(all_tds)
        #summarize_results(run_tests_parallel(all_tds[0:5]))
        #pdb.set_trace()
        
        max_tests = int(options.get("max_tests", False) or len(env_tds))
        test_results = run_tests_parallel(env_tds[0:max_tests])
        summarize_results(
            test_results,
            verbose=options.get('show_all_output',False)
            )

