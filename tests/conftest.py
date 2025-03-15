import pytest
from selene import browser

from tests.models import Product, Cart


@pytest.fixture()
def set_browser_size():
    browser.open('https://google.com')
    browser.driver.maximize_window()

    yield

    browser.quit()


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()
