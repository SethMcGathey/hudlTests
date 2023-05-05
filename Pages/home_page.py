from Pages.base_page import BasePage
from Resources.locators import  LoginPageLocators as loginLocators

#normally would move data like this to a data file to make it reusable
baseUrl = "https://www.hudl.com/"

class HomePage(BasePage):
    
    def __init__(self, driver):
        #sets up driver and navigates to initial page
        super().__init__(driver)
        self.driver.get(baseUrl)
    
    def goToLoginPage(self, ):
        #navigates through the home pages navbar to get to the login page
        self.click(loginLocators.loginSelect)
        self.click(loginLocators.loginHudlFromDropwdown)