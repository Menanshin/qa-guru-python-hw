import os
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from hw_data.utils import attach

DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


@pytest.fixture(scope='function', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def set_browser(request):
    browser_version = request.config.getoption('--browser_version', default=DEFAULT_BROWSER_VERSION) or DEFAULT_BROWSER_VERSION

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    site = os.getenv('SITE')

    if not all([login, password, site]):
        pytest.fail("Не заданы переменные окружения LOGIN, PASSWORD или SITE")

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    try:
        driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@{site}",
            options=options
        )

        browser.config.driver = driver
        browser.config.base_url = 'https://automationexercise.com'
        browser.config.timeout = 10
        browser.config.window_width = 1920
        browser.config.window_height = 1080

        yield browser

    except Exception as e:
        pytest.fail(f"Ошибка при инициализации браузера: {e}")

    finally:
        attach.add_screenshot(browser)
        attach.add_logs(browser)
        attach.add_html(browser)
        attach.add_video(browser)

        browser.quit()


@pytest.fixture(scope='function', autouse=True)
def open_browser(set_browser):
    browser.open('/')
    browser.switch_to_tab(0)