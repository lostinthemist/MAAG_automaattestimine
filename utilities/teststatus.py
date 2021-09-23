"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver


class TestStatus(SeleniumDriver):

    log = cl.customlogger(logging.INFO)

    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        super(TestStatus, self).__init__(driver)
        self.resultlist = []

    def setresult(self, result, resultmessage):
        try:
            if result is not None:
                if result:
                    self.resultlist.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + resultmessage)
                else:
                    self.resultlist.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: + " + resultmessage)
            else:
                self.resultlist.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: + " + resultmessage)
        except:
            self.resultlist.append("FAIL")
            self.log.error("### Exception Occurred !!!")

    def mark(self, result, resultmessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setresult(result, resultmessage)

    def markfinal(self, testname, result, resultmessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.setresult(result, resultmessage)

        if "FAIL" in self.resultlist:
            self.log.error(testname + " ### TEST FAILED")
            self.resultlist.clear()
            assert True == False
        else:
            self.log.info(testname + " ### TEST SUCCESSFUL")
            self.resultlist.clear()
            assert True == True
