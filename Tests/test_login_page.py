import sys
import os
import unittest
from selenium import webdriver
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
        assert self.login_page.is_disabled(loginLocators.loginButtonFromLoginPage), "Login button not disabled"

    def test_invalid_password_valid_username(self):
        self.home_page.goToLoginPage()
        self.login_page.login(userLogin, invalidPassword)
        assert self.login_page.verifyErrorMessage(), "Warning message did not appear."
        assert self.login_page.is_disabled(loginLocators.loginButtonFromLoginPage), "Login button not disabled"

    def test_no_password_valid_login(self):
        self.home_page.goToLoginPage()
        self.login_page.login(userLogin, "")
        assert self.login_page.verifyErrorMessage(), "Warning message did not appear."
        assert self.login_page.is_disabled(loginLocators.loginButtonFromLoginPage), "Login button not disabled"

    def test_no_username_valid_password(self):
        self.home_page.goToLoginPage()
        self.login_page.login("", userPassword)
        assert self.login_page.verifyErrorMessage(), "Warning message did not appear."
        assert self.login_page.is_disabled(loginLocators.loginButtonFromLoginPage), "Login button not disabled"

    def test_no_username_no_password(self):
        self.home_page.goToLoginPage()
        self.login_page.login("", "")
        assert self.login_page.verifyErrorMessage(), "Warning message did not appear."
        assert self.login_page.is_disabled(loginLocators.loginButtonFromLoginPage), "Login button not disabled"

    def test_remember_me_checkbox(self):
        #this test failes because the remember me checkbox does not seem to do anything
        self.home_page.goToLoginPage()
        self.home_page.force_click(loginLocators.rememberMeCheckbox)
        assert self.home_page.is_checked(loginLocators.rememberMeCheckbox)
        self.login_page.login(userLogin, userPassword)
        self.home_page.hover(loginLocators.navbarProfileDropdown)
        self.home_page.click(loginLocators.navbarProfileDropdownLogout)
        self.home_page.goToLoginPage()
        assert self.home_page.is_checked(loginLocators.rememberMeCheckbox), "Remember Me checkbox did not stay checked after logging out"
        assert self.home_page.get_text(loginLocators.emailTextBox) == userLogin, "Email was not stored by the Remember Me checkbox"

    def test_signup_link(self):
        self.home_page.goToLoginPage()
        self.login_page.click(loginLocators.signUpLink)
        assert self.login_page.wait_for_element(loginLocators.signupContentDiv), "Sign up page did not load"
        #In a real project, I would want to have similar tests signing up for accounts and checking all the elements and functionality of the sign up page as well

    def test_back_button(self):
        self.home_page.goToLoginPage()
        self.home_page.click(loginLocators.backButton)
        assert self.login_page.wait_for_element(loginLocators.loginSelect), "Did not return to landing page"

if __name__ == "__main__":
    unittest.main()
