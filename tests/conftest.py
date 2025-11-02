import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")  # без открытия окна браузера
    options.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
