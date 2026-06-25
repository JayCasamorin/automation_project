from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open_url(self, url):
        self.browser.get(url)

    def get_title(self):
        return self.browser.title
    
    def wait_for_title_contains(self, expected_title, timeout=15):
        WebDriverWait(self.browser, timeout).until(
            EC.title_contains(expected_title)
        )

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def find_elements(self, locator, timeout=10):
        WebDriverWait(self.browser, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
        return self.browser.find_elements(*locator)
    
    def click(self, locator, timeout=10):
        element = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def type_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.text
    
    def get_css_property(self, locator, property_name, timeout=10):
        element = self.find_element(locator, timeout)
        return element.value_of_css_property(property_name)
    
    def is_element_displayed(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.is_displayed()
    
    def is_element_enabled(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.is_enabled()
    
    def get_attribute(self, locator, attribute_name, timeout=10):
        element = self.find_element(locator, timeout)
        return element.get_attribute(attribute_name)
    
    def find_present_element(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    def get_text_from_present_element(self, locator, timeout=10):
        element = self.find_present_element(locator, timeout)
        return element.text