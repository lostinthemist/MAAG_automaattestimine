from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class LoginPage(SeleniumDriver):

    log = cl.customlogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "//a[@href='/login']"
    _email_field = "//div[@class='form-group']/input[@type='email']"
    _password_field = "password"
    _login_button = "//input[@type='submit']"

    def clickloginlink(self):
        self.elementclick(self._login_link, locatortype="xpath")

    def enteremail(self, email):
        self.sendkeys(email, self._email_field, locatortype="xpath")

    def enterpassword(self, password):
        self.sendkeys(password, self._password_field)

    def clickloginbutton(self):
        self.elementclick(self._login_button, locatortype="xpath")

    def login(self, email="", password=""):
        self.clickloginlink()
        self.enteremail(email)
        self.enterpassword(password)
        self.clickloginbutton()

    def verifyloginsuccessful(self):
        result = self.iselementpresent("caret",locatortype="class")
        return result

    def verifyloginfailed(self):
        result = self.iselementpresent("//span[@class='dynamic-text help-block']", locatortype="xpath")
        return result

    def verifytitle(self):
        if "My Courses" in self.gettitle():
            return True
        else:
            return False
