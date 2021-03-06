import multiprocessing 
from os.path import join as opj
import subprocess
import tempfile
import datetime
mananage_command = opj(settings.PPY_CODE_ROOT,
              "permalink",
              "manage.py")
def construct_command(test):

    return "python %s test %s --verbosity=0 --noinput" % (mananage_command, test)



def run_test_individually(test):
    os.system(construct_command(test))

def collect_test(test_name):
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
    return (test_name, proc.returncode, end_time - start_time, stds[0], stds[1])

def summarize_results(results):
    fails = []
    for result in results:
        if result[1] != 0:
            fails.append(result)
    print "%d tests run %d failed" % (len(results), len(fails))
    for fail in fails:
        print fail
    print "%d tests run %d failed" % (len(results), len(fails))
            


def run_tests_parallel(tests):
    count = multiprocessing.cpu_count()
    pool=multiprocessing.Pool(processes=count+2)
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
    #ab = collect_test(apps2[0])
    #pdb.set_trace()
    run_tests_parallel(apps2)
    #get_individual_test_names(apps)
    #run_tests(False, verbosity=0)
