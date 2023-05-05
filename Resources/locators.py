from selenium.webdriver.common.by import By

class LoginPageLocators():
    loginSelect = (By.CSS_SELECTOR, "[data-qa-id=login-select]")
    loginHudlFromDropwdown = (By.CSS_SELECTOR, "[data-qa-id=login-hudl]")

    emailLabel = (By.CSS_SELECTOR, "[data-qa-id=email-input-label]")
    emailTextBox = (By.CSS_SELECTOR, "[data-qa-id=email-input]")
    passwordLabel = (By.CSS_SELECTOR, "[data-qa-id=password-input-label]")
    passwordTextBox = (By.CSS_SELECTOR, "[data-qa-id=password-input]")
    rememberMeCheckboxText = (By.CSS_SELECTOR, "[data-qa-id=remember-me-checkbox-label]")
    needHelpHyperlink = (By.CSS_SELECTOR, "[data-qa-id=need-help-link]")
    logInWithOrganizationHyperlink = (By.CSS_SELECTOR, "[data-qa-id=log-in-with-organization-btn]")
    loginButtonFromLoginPage = (By.CSS_SELECTOR, "[data-qa-id=login-btn]")
    invalidLoginWarning = (By.CSS_SELECTOR, "[data-qa-id=error-display]")

    navbarHomeSection = (By.CSS_SELECTOR, "[data-qa-id=webnav-globalnav-home]")