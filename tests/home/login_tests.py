from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("onetimesetup", "setup")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classsetup(self, onetimesetup):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    # Need to verify two verification points
    # 1 fails, code will not go to the next verification point
    # If assert fails, it stops current test execution and
    # moves to the next test method
    @pytest.mark.run(order=2)
    def test_validlogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifytitle()
        self.ts.mark(result1, "Title Verified")
        result2 = self.lp.verifyloginsuccessful()
        self.ts.markfinal("test_validlogin", result2, "Login was successful")

    @pytest.mark.run(order=1)
    def test_invalidlogin(self):
        self.lp.login("test@email.com", "abc")
        result = self.lp.verifyloginfailed()
        assert result == True
