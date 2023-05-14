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
        assert self.get_text(loginLocators.emailLabel) == "Email", "Email label changed"
        assert self.get_text(loginLocators.passwordLabel) == "Password", "Password label changed"
        assert self.get_text(loginLocators.rememberMeCheckboxText) == "Remember me", "Remember Me label changed"
        assert self.get_text(loginLocators.needHelpHyperlink) == "Need help?", "Need Help? label changed"
        assert self.get_text(loginLocators.logInWithOrganizationHyperlink) == "Log In with an Organization", "Log In with an Organization label changed"
        assert self.get_text(loginLocators.loginButtonFromLoginPage) == "Log In" , "Log In label changed"

    def verifyErrorMessage(self):
        return self.get_text(loginLocators.invalidLoginWarning) == "We didn't recognize that email and/or password.Need help?"

