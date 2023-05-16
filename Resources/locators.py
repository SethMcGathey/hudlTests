from selenium.webdriver.common.by import By

class LoginPageLocators():
    loginSelect = (By.CSS_SELECTOR, "[data-qa-id=login-select]")
    loginHudlFromDropwdown = (By.CSS_SELECTOR, "[data-qa-id=login-hudl]")

    emailLabel = (By.CSS_SELECTOR, "[data-qa-id=email-input-label]")
    emailTextBox = (By.CSS_SELECTOR, "[data-qa-id=email-input]")
    passwordLabel = (By.CSS_SELECTOR, "[data-qa-id=password-input-label]")
    passwordTextBox = (By.CSS_SELECTOR, "[data-qa-id=password-input]")
    rememberMeCheckbox = (By.CSS_SELECTOR, "[data-qa-id=remember-me-checkbox]")
    rememberMeCheckboxText = (By.CSS_SELECTOR, "[data-qa-id=remember-me-checkbox-label]")
    needHelpHyperlink = (By.CSS_SELECTOR, "[data-qa-id=need-help-link]")
    logInWithOrganizationHyperlink = (By.CSS_SELECTOR, "[data-qa-id=log-in-with-organization-btn]")
    loginButtonFromLoginPage = (By.CSS_SELECTOR, "[data-qa-id=login-btn]")
    invalidLoginWarning = (By.CSS_SELECTOR, "[data-qa-id=error-display]")
    #example of using the powerful but less desirable/stable xpath
    signUpLink = (By.XPATH, '//a[contains(text(), "Sign up")]')
    backButton = (By.CSS_SELECTOR, "[class=styles_backIcon_1nBYGKhbTIbTmIULDJg1MZ]")

    navbarHomeSection = (By.CSS_SELECTOR, "[data-qa-id=webnav-globalnav-home]")
    navbarProfileDropdown = (By.CSS_SELECTOR, "[class=hui-globaluseritem__display-name]")
    navbarProfileDropdownLogout = (By.CSS_SELECTOR, "[data-qa-id=webnav-usermenu-logout]")

    signupContentDiv = (By.ID, "s_133036-r_1-c_1-copy")

