import unittest

from SampleTest import Testing
from CustomResultListeners import CustomResultListener


def suite():
    suite = unittest.TestSuite()
    suite.addTest(Testing('test_string'))
    suite.addTest(Testing('test_boolean'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
# customResult = CustomResultListener()
# suite().run(customResult)
