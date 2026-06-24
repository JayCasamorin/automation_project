from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class GooglePage(BasePage):
    URL = "https://www.google.com"

    SEARCH_BOX = (By.NAME, "q")

    def open(self):
        self.open_url(self.URL)

    def wait_until_loaded(self):
        self.wait_for_title_contains("Google")

    def is_opened(self):
        return "Google" in self.get_title()
    
    def search(self, text):
        self.type_text(self.SEARCH_BOX, text)
        search_box = self.find_element(self.SEARCH_BOX)
        search_box.send_keys(Keys.ENTER)

    def is_search_results_loaded(self, search_text):
        self.wait_for_title_contains(search_text)
        return search_text in self.get_title()