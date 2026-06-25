from pathlib import Path
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginButton")
    MESSAGE = (By.ID, "message")

    def __init__(self, browser):
        super().__init__(browser)

        project_root = Path(__file__).resolve().parents[1]
        login_file = project_root / "test_site" / "login.html"
        self.URL = login_file.as_uri()

    def open(self):
        self.open_url(self.URL)

    def wait_until_loaded(self):
        self.wait_for_title_contains("Local Login Page")

    def enter_username(self, username):
        self.type_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_message(self):
        return self.get_text(self.MESSAGE)
    
    def get_initial_message(self):
        return self.get_text_from_present_element(self.MESSAGE)
    
    def get_message_color(self):
        return self.get_css_property(self.MESSAGE, "color")
    
    def is_username_field_displayed(self):
        return self.is_element_displayed(self.USERNAME_INPUT)
    
    def is_password_field_displayed(self):
        return self.is_element_displayed(self.PASSWORD_INPUT)
    
    def is_login_button_displayed(self):
        return self.is_element_displayed(self.LOGIN_BUTTON)
    
    def is_login_button_enabled(self):
        return self.is_element_enabled(self.LOGIN_BUTTON)
    
    def get_username_value(self):
        return self.get_attribute(self.USERNAME_INPUT, "value")
    
    def get_password_value(self):
        return self.get_attribute(self.PASSWORD_INPUT, "value")
    
    def get_password_field_type(self):
        return self.get_attribute(self.PASSWORD_INPUT, "type")
    