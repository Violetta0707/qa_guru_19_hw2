
import pytest

from selene import browser

@pytest.fixture(scope="function")
def url():
  browser.open('https://duckduckgo.com')

  yield

  browser.quit()

  @pytest.fixture(scope="function")
  def size_browser():
    browser.config.window_size = (1920, 1080)