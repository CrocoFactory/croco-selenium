import pytest
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(scope="session")
def driver():
    driver = WebDriver()
    yield driver
    driver.close()
