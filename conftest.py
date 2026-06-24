import pytest
from pathlib import Path
from datetime import datetime
from selenium import webdriver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)

@pytest.fixture
def browser(request):
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    if (hasattr(request.node, "rep_call") 
        and request.node.rep_call.failed):
        screenshots_dir = Path("screenshots")
        screenshots_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = request.node.name
        screenshot_path = screenshots_dir / f"{test_name}_{timestamp}.png"

        driver.save_screenshot(str(screenshot_path))

        print(f"\nScreenshot saved: {screenshot_path}")

    driver.quit()

