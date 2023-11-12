from selenium.common import TimeoutException
from croco_selenium_actions import ActionPerformer


def test_ignore_exceptions(driver):
    driver.get('https://google.com')
    action_performer = ActionPerformer(driver)
    action_performer.click(15, '//*[@id="unknownsuchid"]', TimeoutException)
