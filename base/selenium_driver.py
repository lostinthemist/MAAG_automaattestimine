from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging


class SeleniumDriver():

    log = cl.customlogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def gettitle(self):
        return self.driver.title

    def getbytype(self, locatortype):
        locatortype = locatortype.lower()
        if locatortype == "id":
            return By.ID
        elif locatortype == "name":
            return By.NAME
        elif locatortype == "xpath":
            return By.XPATH
        elif locatortype == "css":
            return By.CSS_SELECTOR
        elif locatortype == "class":
            return By.CLASS_NAME
        elif locatortype == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatortype + " not correct/supported")
        return False

    def getelement(self, locator, locatortype="id"):
        element = None
        try:
            locatortype = locatortype.lower()
            bytype = self.getbytype(locatortype)
            element = self.driver.find_element(bytype, locator)
            self.log.info("Element found with locator: " + locator + " and locatortype: " + locatortype)
        except:
            self.log.info("Element not found with locator: " + locator + " and locatortype: " + locatortype)
        return element

    def elementclick(self, locator, locatortype="id"):
        try:
            element = self.getelement(locator, locatortype)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatortype: " + locatortype)
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatortype: " + locatortype)
            print_stack()

    def sendkeys(self, data, locator, locatortype="id"):
        try:
            element = self.getelement(locator, locatortype)
            element.send_keys(data)
            self.log.info("Send data on element with locator: " + locator + " locatortype: " + locatortype)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator + " locatortype: " + locatortype)
            print_stack()

    def iselementpresent(self, locator, locatortype="id"):
        try:
            element = self.getelement(locator, locatortype)
            if element is not None:
                self.log.info("Element found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def elementpresencecheck(self, locator, bytype):
        try:
            elementlist = self.driver.find_elements(bytype, locator)
            if len(elementlist) > 0:
                self.log.info("Element found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitforelement(self, locator, locatortype="id", timeout=10, pollfrequency=0.5):
        element = None
        try:
            # self.driver.implicitly_wait(0)
            bytype = self.getbytype(locatortype)
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((bytype, "stopfilter_stops-0")))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element
