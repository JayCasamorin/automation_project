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