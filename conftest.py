import pytest
from croco_selenium import ChromeDriver


@pytest.fixture(scope="session")
def driver():
    driver = ChromeDriver()
    yield driver
    driver.close()
