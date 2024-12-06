from selene import *
import random
import string


def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


random_text = generate_random_string()


def test_google(set_browser_size):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text(
        'Selene - User-oriented Web UI browser tests in Python'))


def test_google_fail(set_browser_size):
    browser.element('[name="q"]').should(be.blank).type(random_text).press_enter()
    browser.element('[id="search"]').should(have.no.text(
        'Selene - User-oriented Web UI browser tests in Python'))
