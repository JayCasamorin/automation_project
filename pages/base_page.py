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
