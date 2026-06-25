import pytest
from pages.login_page import LoginPage

pytestmark = [pytest.mark.ui, pytest.mark.fields]

@pytest.mark.smoke
def test_login_form_fields_are_displayed(browser):
    login_page = LoginPage(browser)

    login_page.open()
    login_page.wait_until_loaded()

    assert login_page.is_username_field_displayed(), (
        "Username field should be displayed"
    )

    assert login_page.is_password_field_displayed(), (
        "Password field should be displayed"
    )

    assert login_page.is_login_button_displayed(), (
        "Login button should be displayed"
    )

@pytest.mark.smoke
def test_login_button_is_enabled(browser):
    login_page = LoginPage(browser)

    login_page.open()
    login_page.wait_until_loaded()

    assert login_page.is_login_button_enabled(), (
        "Login button should be enabled"
    )

def test_password_field_is_masked(browser):
    login_page = LoginPage(browser)

    login_page.open()
    login_page.wait_until_loaded()

    assert login_page.get_password_field_type() == "password"

def test_message_area_is_empty_before_login(browser):
    login_page = LoginPage(browser)

    login_page.open()
    login_page.wait_until_loaded()

    assert login_page.get_initial_message() == ""

def test_fields_accept_input(browser):
    login_page = LoginPage(browser)

    login_page.open()
    login_page.wait_until_loaded()

    login_page.enter_username("admin")
    login_page.enter_password("admin1234")

    assert login_page.get_username_value() == "admin"
    assert login_page.get_password_value() == "admin1234"