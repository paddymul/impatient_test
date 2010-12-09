"""
This is the file which grabs all the tests and distributes them into separate processes 


"""
from os.path import join as opj
import tempfile
import datetime
import subprocess
import multiprocessing

def construct_command(test):
    man = opj(settings.PPY_CODE_ROOT,
              "permalink",
              "manage.py")

    return "python %s test %s --verbosity=0 --noinput" % (man, test)



def run_test_individually(test):
    os.system("python /home/paddy/permalink/permalink/manage.py test %s --verbosity=0" % test)


class TestResult(object):

    def __init__( self, test_name, return_code,
                  time, stdin, stdout):
        test_name, return_code = self.test_name, self.return_code
        self.time, self.stdin, self.stdout = time, stdin, stdout

        
        

def collect_test(test_name):
    """ so named because it is supposed to collect the data from this
    individual test """
    
    print "starting", test_name
    start_time = datetime.datetime.now()
    proc = subprocess.Popen(
        construct_command(test_name),

        shell=True,
        stdin=subprocess.PIPE,
        stdout=tempfile.TemporaryFile("w"),
        stderr=tempfile.TemporaryFile("w"))

    """
        stdout=subprocess.PIPE)
    """
    stds = proc.communicate()
    end_time = datetime.datetime.now()
    
    print "  finished  ", test_name, proc.returncode
    return TestResult(
        test_name, proc.returncode,
        end_time - start_time, stds[0], stds[1])


def summarize_results(results):
    fails = []
    for result in results:
        if result.return_code != 0:
            fails.append(result)
    print "%d tests run %d failed" % (len(results), len(fails))
    for fail in fails:
        print fail
    print "%d tests run %d failed" % (len(results), len(fails))
            


def run_tests_parallel(tests):
    count = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=count+2)
    results = pool.map(collect_test, tests)
    summarize_results(results)

    
def run_all_tests_individually():
    test_list = get_individual_test_names(get_apps())
    for test in test_list:
        print test
        run_test_individually(test)
        #pdb.set_trace()


        
if __name__== "__main__":
    apps2 = get_individual_test_names(get_filtered_apps())
    #apps2 = get_individual_test_names([get_app("proxy")])
    #apps2 = get_individual_test_names([get_app("access")])
    #ab = collect_test(apps2[0])
    #pdb.set_trace()
    run_tests_parallel(apps2)
    #get_individual_test_names(apps)
    #run_tests(False, verbosity=0)
