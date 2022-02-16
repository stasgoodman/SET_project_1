from tests.base import *
from tests.test_catapi import *


def run_catapi_tests():
    test_suite = unittest.TestLoader().loadTestsFromTestCase(Test1stCatApi)
    unittest.TextTestRunner(verbosity=2).run(test_suite)


def run_2_catapi_tests():
    test_suite = unittest.TestLoader().loadTestsFromTestCase(Test2ndCatApi)
    unittest.TextTestRunner(verbosity=2).run(test_suite)


def run_3_catapi_tests():
    test_suite = unittest.TestLoader().loadTestsFromTestCase(Test3ndCatApi)
    unittest.TextTestRunner(verbosity=2).run(test_suite)
