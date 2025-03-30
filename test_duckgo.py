
import pytest
from selene import have, be, by
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.window_width = 1280
    browser.config.window_height = 800
    yield
    browser.quit()


def test_duckgo_search_should_find_results():
    browser.open('https://duckduckgo.com')

    try:
        browser.element(by.text('Accept all')).click()
    except:
        pass

    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('#search').should(have.text('yashaka/selene'))


def test_duckgo_search_should_not_find_results():
    browser.open('https://duckduckgo.com')

    try:
        browser.element(by.text('Accept all')).click()
    except:
        pass

    nonsense_query = 'ghkgujh'
    browser.element('[name="q"]').should(be.blank).type(nonsense_query).press_enter()
    browser.element('body').should(have.text('результаты не найдены'))
