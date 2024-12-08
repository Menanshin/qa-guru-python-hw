import pytest
from selene import browser


@pytest.fixture()
def set_browser_size():
    browser.open('https://google.com')
    browser.driver.maximize_window()

    yield

    browser.quit()