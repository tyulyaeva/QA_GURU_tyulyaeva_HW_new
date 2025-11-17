import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_setup():
    browser.config.driver_name = "chrome"
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_width = "1280"
    browser.config.window_height = "900"
    browser.config.timeout = 6

    yield
    browser.quit()