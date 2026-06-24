import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize(
    "username, password, expected_message",
    [
        ("admin", "admin1234", "LOGIN SUCCESS"),
        ("admin", "wrongpass", "LOGIN FAILED"),
        ("wronguser", "admin1234", "LOGIN FAILED"),
        ("", "admin1234", "LOGIN FAILED"),
        ("admin", "", "LOGIN FAILED"),
    ],
    ids=[
        "TC_LOGIN_001_valid_credentials",
        "TC_LOGIN_002_invalid_password",
        "TC_LOGIN_003_invalid_username",
        "TC_LOGIN_004_blank_username",
        "TC_LOGIN_005_blank_password",
    ]
)
def test_local_login(browser, username, password, expected_message):
    login_page = LoginPage(browser)

    login_page.open()
    login_page.wait_until_loaded()
    login_page.login(username, password)

    actual_message = login_page.get_message()

    assert actual_message == expected_message, (
        f"Expected {expected_message}, but got {actual_message}"
    )

