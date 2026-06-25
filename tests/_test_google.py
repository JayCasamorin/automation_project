from pages.google_page import GooglePage

def test_open_google(browser):
    google_page = GooglePage(browser)

    google_page.open()
    google_page.wait_until_loaded()

    assert google_page.is_opened()

def test_google_search(browser):
    google_page = GooglePage(browser)

    google_page.open()
    google_page.wait_until_loaded()
    google_page.search("Selenium Python")

    assert google_page.is_search_results_loaded("Selenium Python")