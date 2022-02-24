import unittest

from Test.DBTest import DBTest
from Test.ParametrizedTestCase import ParametrizedTestCase
import os

from Test.SparkTest import SparkTest


# def suite():
#     """
#         Gather all the tests from this module in a test suite.
#     """
#     test_suite = unittest.TestSuite()
#     test_suite.addTest(DBTest("test_db_connection"))
#     # test_suite.addTest(unittest.makeSuite(SparkTest))
#     return test_suite

# suite = unittest.TestSuite()
# config_file_path = os.path.join(os.path.dirname(__file__), 'config', 'config.ini')
# suite.addTest(ParametrizedTestCase.parametrize(DBTest, param=config_file_path))
# # suite.addTest(ParametrizedTestCase.parametrize(TestOne, param=13))
# unittest.TextTestRunner().run(suite)


# config_file_path = os.path.join(os.path.dirname(__file__), 'config', 'config.ini')
# suite.addTest(ParametrizedTestCase.parametrize(DBTest, param=config_file_path))
# # suite.addTest(ParametrizedTestCase.parametrize(TestOne, param=13))
#
# suite = unittest.TestSuite()
# unittest.TextTestRunner().run(suite)



def suite():
    suite = unittest.TestSuite()
    # suite.addTest(DBTest('test_db_connection'))
    # suite.addTest(DBTest('test_something_else'))
    # suite.addTest(SparkTest('test_pyspark'))
    suite.addTest(SparkTest('test_pysaprk_column_type'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())