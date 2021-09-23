"""
@package base

Webdriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class
        :return:
        None
        :param browser:
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer enviroment bassed on OS
        
        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        
        PREFERRED: Set the path on the machine where browser will be executed
    """


    def getwebdriverinstance(self):
        """
        Get WebDriver Instance based on the browser configuration
        :return:
            'WebDriver.Instance'
        """
        base_url = "https://courses.letskodeit.com/"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(5)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with app URL
        driver.get(base_url)
        return driver
