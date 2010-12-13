"""
This is the file which grabs all the tests and distributes them into separate processes 


"""
from os.path import join as opj
import tempfile
import datetime
import subprocess
import multiprocessing
from django.conf import settings
import pdb
import os

def construct_command(test):
    man = opj(settings.CODE_ROOT, settings.PROJ_NAME, "manage.py")
    return "python %s test %s --verbosity=0 --noinput" % (man, test)



def run_test_individually(test):
    os.system(construct_command(test))


class TestResult(object):

    def __init__( self, test_name, return_code,
                  time, stdout, stderr):
        self.test_name, self.return_code = test_name, return_code
        self.time, self.stdout, self.stderr = time, stdout, stderr

    def __str__(self):

        
        v = [self.test_name, self.return_code,
             self.time, self.stdout, self.stderr]
        v=map(str,v)
        seperator = "\n" + "@"*80 + "\n"
        #pdb.set_trace()
        return seperator.join(v)

    def __repr__(self):
        return self.__str__()
        
        

def collect_test(test_description):
    """ so named because it is supposed to collect the data from this
    individual test """
    #pdb.set_trace()
    print test_description
    test_name = test_description.invoke_string
    env = test_description.env
    print "starting", test_name
    os.environ.update(env)
    start_time = datetime.datetime.now()
    stdout_temp = tempfile.TemporaryFile("rw")
    stderr_temp = tempfile.TemporaryFile("rw")
    proc = subprocess.Popen(
        construct_command(test_name),
        shell=True,
        stdin=subprocess.PIPE,
        stdout=stdout_temp,
        stderr=stderr_temp)
    stds = proc.communicate()
    end_time = datetime.datetime.now()

    

    # need to seek to 0 so that we can read from this file
    stdout_temp.seek(0)
    stderr_temp.seek(0)
    
    print "  finished  ", test_name, proc.returncode
    return TestResult(
        test_name, proc.returncode,
        end_time - start_time,
        stdout_temp.read(),
        stderr_temp.read())


def run_tests_parallel(tests):
    count = multiprocessing.cpu_count()
    #pool = multiprocessing.Pool(processes=count+2)
    pool = multiprocessing.Pool(processes=1)
    results = pool.map(collect_test, tests)
    return results
    #summarize_results(results)



def summarize_results(results):
    fails = []
    for result in results:
        if result.return_code != 0:
            fails.append(result)
    print "%d tests run %d failed" % (len(results), len(fails))
    print "\n\n\n"
    print "individual failing test outputs "
    for fail in fails:
        print "+"*80
        print fail
        print "+"*80
    print "\n\n\n"
    print "%d tests run %d failed" % (len(results), len(fails))
            
    
def run_all_tests_individually():
    test_list = get_individual_test_names(get_apps())
    for test in test_list:
        print test
        run_test_individually(test)



        
if __name__== "__main__":
    #apps2 = get_individual_test_names(get_filtered_apps())
    #apps2 = get_individual_test_names([get_app("proxy")])
    #apps2 = get_individual_test_names([get_app("access")])
    #ab = collect_test(apps2[0])
    #pdb.set_trace()
    #run_tests_parallel(apps2)
    #get_individual_test_names(apps)
    #run_tests(False, verbosity=0)
    pass
