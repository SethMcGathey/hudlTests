import sys
import os
import unittest

from base_test import BaseTest

#Allows python to find the imports below
base_dir = os.path.dirname(__file__) or '.'
sys.path.append("..")

from Resources.locators import LoginPageLocators as loginLocators
from Pages.home_page import HomePage
from Pages.login_page import LoginPage

#normally would be in a gitignored dataFile
############# Enter a valid email and password ###############
userLogin = "seth.mcgathey@gmail.com"
userPassword = "1qaz2wsx!Q"
############# Enter a valid email and password ###############

invalidLogin = "notValid@gmail.com"
invalidPassword = "invalidPassword123"

class TestLoginTests(BaseTest):
    def setUp(self):
        super().setUp()
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
    
    def test_unauthenticated_user_cannot_access(self):
        self.driver.get("https://www.hudl.com/home")
        #confirm page redirected to login instead of homepage
        assert loginLocators.emailTextBox

    def test_valid_login(self):
        self.home_page.goToLoginPage()
        self.login_page.verifyLoginPage()
        self.login_page.login(userLogin, userPassword)
        #check for the navbar of the home screen to verify that login worked
        assert self.login_page.wait_for_element(loginLocators.navbarHomeSection), "Navbar not found, login failed"

    def test_invalid_username_valid_password(self):
        self.home_page.goToLoginPage()
        self.login_page.login(invalidLogin, userPassword)
        assert self.login_page.verifyErrorMessage(), "Warning message did not appear."

    def test_invalid_password_valid_username(self):
        self.home_page.goToLoginPage()
        self.login_page.login(userLogin, invalidPassword)
        assert self.login_page.verifyErrorMessage(), "Warning message did not appear."

    def test_no_password_valid_login(self):
        self.home_page.goToLoginPage()
        self.login_page.login(userLogin, "")
        assert self.login_page.verifyErrorMessage(), "Warning message did not appear."

    def test_no_username_valid_password(self):
        self.home_page.goToLoginPage()
        self.login_page.login("", userPassword)
        assert self.login_page.verifyErrorMessage(), "Warning message did not appear."

if __name__ == "__main__":
    unittest.main()
