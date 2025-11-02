import pytest


@pytest.mark.github
def test_github_web_find_current_url(driver):
    url = "https://github.com/"
    driver.get(url)

    assert "GitHub" in driver.title
    assert driver.current_url == url
