import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.google
def test_google_search(driver):
    url = "https://www.google.com/"
    driver.get(url)
    search_value = "selenide"

    assert driver.title == "Google"
    assert driver.current_url == url

    element_google = driver.find_element(By.NAME, "q")
    element_google.send_keys(search_value)
    element_google.submit()

    time.sleep(10)
    assert search_value in driver.page_source
