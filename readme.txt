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
** to run
cd into proj_impatient_demo/
python manage.py i_test


** to install into your project
look at proj_impatient_demo/settings.py to see hwo impatient_test is
used.  This project also happens to be part of the impatient_test
test_suite

