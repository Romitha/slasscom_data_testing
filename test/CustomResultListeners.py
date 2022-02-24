import unittest


class CustomResultListener(unittest.TestResult):


    def startTest(self, test):
        print('Starting test : ', test)

    def stopTest(self, test):
        print('Stopping test : ', test)

    def addFailure(self, test, err):
        print("Failed test : ", test, " with error ", err)

    def addSuccess(self, test):
        print("test passed : ", test)

    def addSkip(self, test, reason):
        print("test skipped : ", test, "with reason : ", reason)

    def addExpectedFailure(self, test, err):
        print("test Expected Failure : ", test, "with reason ", err)

    def addUnexpectedSuccess(self, test):
        print("test UnExpected Passed : ", test)