
from django.conf import settings

if not settings.PROJ_NAME == "impatient_test_fixtures":
    settings.SKIP_TESTS += ("impatient_test",)
    import pdb
    print settings.SKIP_TESTS
    #pdb.set_trace()
    print settings.SKIP_TESTS

    

