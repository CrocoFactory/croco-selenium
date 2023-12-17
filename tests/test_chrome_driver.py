import time
import pytest
from croco_selenium import ChromeDriver


@pytest.fixture
def driver():
    return ChromeDriver()


def test_click(driver):
    driver.get('https://facebook.com')
    driver.send_keys(15, '//input[@id="email"]', 'hello@world.com')
    time.sleep(15)
