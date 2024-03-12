import json
import time
import random
from typing import Optional
from selenium.webdriver.chromium.webdriver import ChromiumDriver as WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from .types import XPATH, IgnoredExceptions, Cookies
from .utils import ignore_exceptions

__all__ = [
    'add_cookies',
    'switch_to_another_window',
    'switch_to_parent_frame',
    'switch_to_frame',
    'send_keys',
    'silent_send_keys',
    'click',
    'get_elements',
    'get_element',
    'get_element_text',
    'get_element_attribute',
    'wait_for_invisibility',
    'wait_for_windows',
    'close_tabs'
]


def add_cookies(driver: WebDriver, cookies: Cookies) -> None:
    """
    Adds cookies to a current page
    :param driver: A driver to be interacted
    :param cookies: List of dictionaries or dictionary containing cookies
    :return: None
    """
    cookies = json.loads(cookies) if isinstance(cookies, str) else cookies

    if isinstance(cookies, list):
        for cookie in cookies:
            if 'domain' in cookie:
                driver.add_cookie(cookie)
    elif isinstance(cookies, dict):
        if 'domain' in cookies:
            driver.add_cookie(cookies)


def switch_to_another_window(driver: WebDriver, timeout: float = 100) -> None:
    """
    Switches to a different window from current window in browser
    :param driver: A driver to be interacted
    :param timeout: Number of seconds before timing out

    :return: str
    """
    original_window_handle = driver.current_window_handle
    WebDriverWait(driver, timeout).until(EC.number_of_windows_to_be(2))

    for window_handle in driver.window_handles:
        if window_handle != original_window_handle:
            driver.switch_to.window(window_handle)
            break


@ignore_exceptions
def switch_to_frame(
        driver: WebDriver,
        timeout: float,
        xpath: XPATH,
        *,
        ignored_exceptions: Optional[IgnoredExceptions] = None
) -> None:
    """
    Switches to the frame
    :param driver: A driver to be interacted
    :param timeout: Number of seconds before timing out
    :param xpath: XPATH of an element
    :param ignored_exceptions: Tuple of ignored exceptions or one ignoring exception

    :return: None
    """
    WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions).until(
        EC.frame_to_be_available_and_switch_to_it(
            (By.XPATH, xpath)))


def switch_to_parent_frame(
        driver: WebDriver
) -> None:
    """
    Switches to the parent frame
    :param driver: A driver to be interacted
    :return: None
    """
    driver.switch_to.parent_frame()


@ignore_exceptions
def send_keys(
        driver: WebDriver,
        timeout: float,
        xpath: XPATH,
        text: str,
        cleared: bool = True,
        *,
        ignored_exceptions: Optional[IgnoredExceptions] = None
) -> None:
    """
    Sends keys in browser
    :param driver: A driver to be interacted
    :param timeout: Number of seconds before timing out
    :param xpath: XPATH of an element
    :param text: Text to send
    :param ignored_exceptions: Tuple of ignored exceptions or one ignoring exception
    :param cleared: If true, field clears before be interacted

    :return: None
    """
    element = WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions).until(
        EC.element_to_be_clickable(
            (By.XPATH, xpath)))

    if cleared:
        element.clear()

    element.send_keys(text)


@ignore_exceptions
def silent_send_keys(
        driver: WebDriver,
        timeout: float,
        xpath: XPATH,
        text: str,
        cleared: bool = True,
        min_delay: float = 0.07,
        max_delay: float = 0.14,
        *,
        ignored_exceptions: Optional[IgnoredExceptions] = None
) -> None:
    """
    Sends keys with delay between characters in browser
    :param driver: A driver to be interacted
    :param timeout: Number of seconds before timing out
    :param xpath: XPATH of an element
    :param text: Text to send
    :param ignored_exceptions: Tuple of ignored exceptions or one ignoring exception
    :param cleared: If true, field clears before be interacted
    :param min_delay: Minimum delay between sending a character
    :param max_delay: Maximum delay between sending a character

    :return: None
    """
    element = WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions).until(
        EC.element_to_be_clickable(
            (By.XPATH, xpath)))

    if cleared:
        element.clear()

    for char in text:
        element.send_keys(char)
        delay = random.uniform(min_delay, max_delay)
        time.sleep(delay)


@ignore_exceptions
def click(
        driver: WebDriver,
        timeout: float,
        xpath: XPATH,
        *,
        ignored_exceptions: Optional[IgnoredExceptions] = None
) -> None:
    """
    Clicks on element in browser
    :param driver: A driver to be interacted
    :param timeout: Number of seconds before timing out
    :param xpath: XPATH of an element
    :param ignored_exceptions: Tuple of ignored exceptions or one ignoring exception

    :return: None
    """
    WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions).until(
        EC.element_to_be_clickable(
            (By.XPATH, xpath))).click()


@ignore_exceptions
def get_element_text(
        driver: WebDriver,
        timeout: float,
        xpath: XPATH,
        *,
        ignored_exceptions: Optional[IgnoredExceptions] = None
) -> str:
    """
    Returns element's text in browser
    :param driver: A driver to be interacted
    :param timeout: Number of seconds before timing out
    :param xpath: XPATH of an element
    :param ignored_exceptions: Tuple of ignored exceptions or one ignoring exception

    :return: str
    """
    return WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath))).text


@ignore_exceptions
def get_element_attribute(
        driver: WebDriver,
        timeout: float,
        xpath: XPATH,
        attribute: str,
        *,
        ignored_exceptions: Optional[IgnoredExceptions] = None
) -> str:
    """
    Returns an element's attribute in browser
    :param driver: A driver to be interacted
    :param timeout: Number of seconds before timing out
    :param xpath: XPATH of an element
    :param attribute: Name of an attribute of the element
    :param ignored_exceptions: Tuple of ignored exceptions or one ignoring exception

    :return: str
    """
    return WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath))).get_attribute(attribute)


@ignore_exceptions
def get_element(
        driver: WebDriver,
        timeout: float,
        xpath: XPATH,
        visible: bool = True,
        *,
        ignored_exceptions: Optional[IgnoredExceptions] = None
) -> WebElement:
    """
    Returns an element in browser
    :param driver: A driver to be interacted
    :param timeout: Number of seconds before timing out
    :param xpath: XPATH of an element
    :param visible: Whether element should be visible
    :param ignored_exceptions: Tuple of ignored exceptions or one ignoring exception

    :return: WebElement
    """
    if visible:
        condition = EC.visibility_of_element_located((By.XPATH, xpath))
    else:
        condition = EC.presence_of_element_located((By.XPATH, xpath))

    return WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions).until(condition)


@ignore_exceptions
def get_elements(
        driver: WebDriver,
        timeout: float,
        xpath: XPATH,
        visible: bool = True,
        *,
        ignored_exceptions: Optional[IgnoredExceptions] = None
) -> list[WebElement]:
    """
    Returns elements in browser
    :param driver: A driver to be interacted
    :param timeout: Number of seconds before timing out
    :param xpath: XPATH of an element
    :param visible: Whether element should be visible
    :param ignored_exceptions: Tuple of ignored exceptions or one ignoring exception

    :return: list[WebElement]
    """
    if visible:
        condition = EC.visibility_of_all_elements_located((By.XPATH, xpath))
    else:
        condition = EC.presence_of_all_elements_located((By.XPATH, xpath))

    return WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions).until(condition)


@ignore_exceptions
def wait_for_invisibility(
        driver: WebDriver,
        timeout: float,
        xpath: XPATH,
        *,
        ignored_exceptions: Optional[IgnoredExceptions] = None
) -> None:
    """
    Wait for element's invisibility in browser
    :param driver: A driver to be interacted
    :param timeout: Number of seconds before timing out
    :param xpath: XPATH of an element
    :param ignored_exceptions: Tuple of ignored exceptions or one ignoring exception

    :return: None
    """
    WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions).until(
        EC.invisibility_of_element_located(
            (By.XPATH, xpath)))
    time.sleep(1)


@ignore_exceptions
def wait_for_windows(
        driver: WebDriver,
        timeout: float,
        number: int,
        *,
        ignored_exceptions: Optional[IgnoredExceptions] = None
) -> None:
    """
    Wait for occurring of number of windows
    :param driver: A driver to be interacted
    :param timeout: Number of seconds before timing out
    :param number: Number of windows to be waited
    :param ignored_exceptions: Tuple of ignored exceptions or one ignoring exception

    :return: None
    """
    WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions).until(
        EC.number_of_windows_to_be(number))
    time.sleep(1)


def close_tabs(driver: WebDriver) -> None:
    """
    Closes all tabs in browser
    :param driver: A driver to be interacted

    :return: None
    """
    original_window_handle = driver.current_window_handle
    windows = driver.window_handles
    for window in windows:
        if original_window_handle != window:
            driver.switch_to.window(window)
            driver.close()
    driver.switch_to.window(original_window_handle)
