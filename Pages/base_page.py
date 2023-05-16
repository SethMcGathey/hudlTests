from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class BasePage():
    #Putting the most common functionality in one place and simplifying the use of those functions
    def __init__(self, driver):
        #This function is called when an object of the base class is created
        self.driver = driver
    
    def click(self, by_locator):
        #Click provided element
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).click()
    
    def enter_text(self, by_locator, text):
        #Send provided text to provided element
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator) -> str:
        #Returns the text of the element provided
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_title(self, title) -> str:
        #Returns the page title
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def wait_for_element(self, by_locator):
        #wait for element to be present on the page
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
    
    def is_checked(self, by_locator):
        #check if a checkbox has been checked or not
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_selected()

    def force_click(self, by_locator):
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)))
    
    def hover(self, by_locator):
        a = ActionChains(self.driver)
        a.move_to_element(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))).perform()

    def is_enabled(self, by_locator):
        #check if a checkbox has been checked or not
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_enabled()

    def is_disabled(self, by_locator):
        #check if a checkbox has been checked or not
        return not WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_enabled()

