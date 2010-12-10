

import unittest
import sys

stdout_string = "^^^^8798^^^^^"

stderr_string = "%%%%8798%%%%"
class OutputTestKlass(unittest.TestCase):

    def test_stdout(self):
        """writes the stderr_string to stderr """
        sys.stdout.write(stdout_string)

    def test_stderr(self):
        """writes the stderr_string to stderr """
        sys.stderr.write(stderr_string)

if __name__ == '__main__':
    unittest.main()









