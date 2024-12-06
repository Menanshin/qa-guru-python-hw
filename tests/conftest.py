import pytest
from selene import browser


@pytest.fixture()
def set_browser_size():
    browser.driver.maximize_window()
    #browser.config.window_width = 1496
    #browser.config.window_height = 836
    yield
    browser.quit()
