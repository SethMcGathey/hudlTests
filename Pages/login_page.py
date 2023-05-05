from Pages.base_page import BasePage
from Resources.locators import LoginPageLocators as loginLocators

class LoginPage(BasePage):
    def login(self, userLogin, userPassword):
        #takes in the username and password and logs in
        self.enter_text(loginLocators.emailTextBox, userLogin)
        self.enter_text(loginLocators.passwordTextBox, userPassword)
        self.click(loginLocators.loginButtonFromLoginPage)

    def verifyLoginPage(self):
        #Checks that the text of the Login page are displayed properly
        assert self.get_text(loginLocators.emailLabel) == "Email"
        assert self.get_text(loginLocators.passwordLabel) == "Password"
        assert self.get_text(loginLocators.rememberMeCheckboxText) == "Remember me"
        assert self.get_text(loginLocators.needHelpHyperlink) == "Need help?"
        assert self.get_text(loginLocators.logInWithOrganizationHyperlink) == "Log In with an Organization"
        assert self.get_text(loginLocators.loginButtonFromLoginPage) == "Log In"

    def verifyLoginWorked(self):
        #check for the navbar of the home screen to verify that login worked
        self.wait_for_element(loginLocators.navbarHomeSection)
        