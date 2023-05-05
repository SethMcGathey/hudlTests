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
userLogin = ""
userPassword = ""
############# Enter a valid email and password ###############

invalidLogin = "notValid@gmail.com"

class TestLoginTests(BaseTest):
    def setUp(self):
        super().setUp()
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)

    def test_valid_login(self):
        self.home_page.goToLoginPage()
        self.login_page.verifyLoginPage()
        self.login_page.login(userLogin, userPassword)
        self.login_page.verifyLoginWorked()

    def test_invalid_login(self):
        self.home_page.goToLoginPage()
        self.login_page.verifyLoginPage()
        self.login_page.login(invalidLogin, userPassword)
        assert self.home_page.get_text(loginLocators.invalidLoginWarning) == "We didn't recognize that email and/or password.Need help?"


if __name__ == "__main__":
    unittest.main()