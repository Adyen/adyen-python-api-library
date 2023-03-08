import unittest
import sys

test_loader = unittest.TestLoader()
tests = test_loader.discover('test/methodNamesTests', pattern='*Test.py')
test_runner = unittest.TextTestRunner()
test_results = test_runner.run(tests)
if test_results.wasSuccessful():
    sys.exit(0)
else:
    sys.exit(1)