-*- mode: org; -*-

* purpose
** django unit tests run very slowly
Multi-core machines are now incredibly common. Impatient test lets you
take advantadge of them.  With a superfast test suite, you can use
your unit tests like you use syntax highlighting - to quickly show you
errors in your code

** sqlite3 is much faster than mysql
sqlite3 is much much faster than mysql, but not all tests can run
against sqlite3, some require a different database engine. With django
you need to use the same database engine for every test, since
impatient_test runs each test in a separate process, you can choose
which engine to use on a per test basis.

** better reporting
impatient_test capture separate std_out and std_err for each
individual test.  Along with the runtime for each test.  This lets you
see which parts are taking longer than others and better diagnose
errors.

* how
** run the demo
cd into proj_impatient_demo/
python manage.py i_test

you will see some output about each test running, then at the end you
will see the information for the one failing test
(There is a failing test in proj_impatient_demo to test that
impatient_test can recognize failed tests )

you can also run
python manage.py test
to run the traditional tests



** to install into your project
look at proj_impatient_demo/settings.py to see hwo impatient_test is
used.  This project also happens to be part of the impatient_test
test_suite
*** restrictions
impatient_test currently only works with sqlite3, code for other
databases is coming soon.


* what

** a rewrite of the django test discovery engine
django's test discovery engine works, but it is very brittle.  tests
are only dealt with as strings "app_name.TestKlass.test_case".  
look at "django.test.simple.build_test"

This makes it hard to programatically manipulate which tests are run.  To
mitigate this problem impatient_test finds every test case, and for
each, constructs a TestDescription object
"impatient_test.find_all_tests.TestDescription" 

Since TestDescription objects have a reference to the actual function,
we can find out much more information about any single testcase, we
can annotate it (a note saying that it requires mysql, or that it is
expected to fail).  

This code isn't as clean as I would like yet, but it is on its way.
Filtering a list of TestDescription objects will be much easier than
filtering a bunch of strings.  look at the gymnastics the
django-test-extensions
(https://github.com/garethr/django-test-extensions) project has to go
through to exclude certain apps from being tested  

in general impatient_test tries to use many small composeable
functions instead of a few big monolithic functions


Eventually we want a rich set of tools for filtering and scheduling
tests so that they can be run quickly.  (run tests that failed on the
last run first)

