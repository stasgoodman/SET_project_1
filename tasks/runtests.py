from tests.test_catapi import *


def run_catapi_tests():
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestCatApi)
    unittest.TextTestRunner(verbosity=2).run(test_suite)

