import pytest
from pathlib import Path
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

RUN_TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")

def clean_filename(name):
    return (
        name.replace("[", "_")
            .replace("]", "")
            .replace("/", "_")
            .replace("\\", "_")
            .replace(":", "_")
            .replace(" ", "_")
    )

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="edge",
        choices=["edge", "chrome"],
        help="Browser to run tests against: edge or chrome"
    )

    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browswer in headless mode"
    )

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser_name == "edge":
        options = EdgeOptions()

        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")

        driver = webdriver.Edge(options=options)

    elif browser_name == "chrome":
        options = ChromeOptions()

        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshots_dir = Path("screenshots") / RUN_TIMESTAMP
        screenshots_dir.mkdir(parents=True, exist_ok=True)

        test_name = clean_filename(request.node.name)
        screenshot_path = screenshots_dir / f"{test_name}.png"

        driver.save_screenshot(str(screenshot_path))

        print(f"\nScreenshot saved: {screenshot_path}")

    driver.quit