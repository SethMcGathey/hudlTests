import unittest
from selenium import webdriver

baseUrl = "https://www.hudl.com/"
class BaseTest(unittest.TestCase):
    def setUp(self):
        #setup drivers and url
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(baseUrl)

    def tearDown(self):
        #free up the driver after test is done
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()