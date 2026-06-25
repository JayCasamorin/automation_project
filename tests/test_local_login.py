import json
from pathlib import Path
import pytest
from pages.login_page import LoginPage

pytestmark = [pytest.mark.ui, pytest.mark.login, pytest.mark.regression]

def load_login_test_data():
    project_root = Path(__file__).resolve().parents[1]
    data_file = project_root / "test_data" / "login_test_data.json"

    with open(data_file, "r") as file:
        return json.load(file)


test_data = load_login_test_data()


@pytest.mark.parametrize(
    "test_case",
    test_data,
    ids=[case["id"] for case in test_data]
)
def test_local_login(browser, test_case):
    login_page = LoginPage(browser)

    login_page.open()
    login_page.wait_until_loaded()
    login_page.login(
        test_case["username"],
        test_case["password"]
    )

    actual_message = login_page.get_message()
    expected_message = test_case["expected_message"]

    actual_color = login_page.get_message_color()
    expected_color = test_case["expected_color"]

    assert actual_message == expected_message, (
        f"Expected message {expected_message}, but got {actual_message}."
        f"Ref: {test_case['id']}"
    )

    assert actual_color == expected_color, (
        f"Expected color {expected_color}, but got {actual_color}. "
        f"Ref: {test_case['id']}"
    )