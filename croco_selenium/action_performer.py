from typing import Optional
from selenium.webdriver.remote.webelement import WebElement
from .types import XPATH, IgnoredExceptions, Cookies
from selenium.webdriver.chromium.webdriver import ChromiumDriver as WebDriver
from .actions import *


class ActionPerformer:
    """The class performing actions in specified driver, such as clicking, sending keys etc"""
    def __init__(self, driver: WebDriver):
        """
        :param driver: A driver to be interacted
        """
        self.__targeted_driver = driver

    def add_cookies(self, cookies: Cookies) -> None:
        """
        Adds cookies to browser
        :param cookies: List of dictionaries or dictionary containing cookies
        :return: None
        """
        driver = self.__targeted_driver
        add_cookies(driver, cookies)

    def switch_to_another_window(self, timeout: float = 100) -> None:
        """
        Switches to a different window from current window in browser
        :param timeout: Number of seconds before timing out

        :return: None
        """
        driver = self.__targeted_driver
        switch_to_another_window(driver, timeout)

    def switch_to_frame(
            self,
            timeout: float,
            xpath: XPATH,
            *,
            ignored_exceptions: Optional[IgnoredExceptions] = None
    ) -> None:
        """
        Switches to the frame
        :param timeout: Number of seconds before timing out
        :param xpath: XPATH of an element
        :param ignored_exceptions: Tuple of ignored exceptions or one ignored exception

        :return: None
        """
        driver = self.__targeted_driver
        switch_to_frame(driver, timeout, xpath, ignored_exceptions=ignored_exceptions)

    def switch_to_parent_frame(
            self
    ) -> None:
        """
        Switches to the parent frame
        :return: None
        """
        driver = self.__targeted_driver
        switch_to_parent_frame(driver)

    def send_keys(
            self,
            timeout: float,
            xpath: XPATH,
            text: str,
            ignored_exceptions: Optional[IgnoredExceptions] = None,
            cleared: bool = True
    ) -> None:
        """
        Sends keys in browser
        :param timeout: Number of seconds before timing out
        :param xpath: XPATH of an element
        :param text: Text to send
        :param ignored_exceptions: Tuple of ignored exceptions or one ignored exception
        :param cleared: If true, field clears before be interacted

        :return: None
        """
        driver = self.__targeted_driver
        send_keys(driver, timeout, xpath, text, cleared, ignored_exceptions=ignored_exceptions)

    def silent_send_keys(
            self,
            timeout: float,
            xpath: XPATH,
            text: str,
            ignored_exceptions: Optional[IgnoredExceptions] = None,
            cleared: bool = True,
            min_delay: float = 0.07,
            max_delay: float = 0.14
    ) -> None:
        """
        Sends keys with delay between characters in browser
        :param timeout: Number of seconds before timing out
        :param xpath: XPATH of an element
        :param text: Text to send
        :param ignored_exceptions: Tuple of ignored exceptions or one ignored exception
        :param cleared: If true, field clears before be interacted
        :param min_delay: Minimum delay between sending a character
        :param max_delay: Maximum delay between sending a character

        :return: None
        """
        driver = self.__targeted_driver
        silent_send_keys(
            driver,
            timeout,
            xpath,
            text,
            cleared,
            min_delay,
            max_delay,
            ignored_exceptions=ignored_exceptions
        )

    def click(
            self,
            timeout: float,
            xpath: XPATH,
            ignored_exceptions: Optional[IgnoredExceptions] = None
    ) -> None:
        """
        Clicks on element in browser
        :param timeout: Number of seconds before timing out
        :param xpath: XPATH of an element
        :param ignored_exceptions: Tuple of ignored exceptions or one ignored exception

        :return: None
        """
        driver = self.__targeted_driver
        click(driver, timeout, xpath, ignored_exceptions=ignored_exceptions)

    def get_element_text(
            self,
            timeout: float,
            xpath: XPATH,
            ignored_exceptions: Optional[IgnoredExceptions] = None
    ) -> str:
        """
        Gets element's text in browser
        :param timeout: Number of seconds before timing out
        :param xpath: XPATH of an element
        :param ignored_exceptions: Tuple of ignored exceptions or one ignored exception

        :return: str
        """
        driver = self.__targeted_driver
        return get_element_text(driver, timeout, xpath, ignored_exceptions=ignored_exceptions)

    def get_element_attribute(
            self,
            timeout: float,
            xpath: XPATH,
            attribute: str,
            ignored_exceptions: Optional[IgnoredExceptions] = None
    ) -> str:
        """
        Gets element's attribute in browser
        :param timeout: Number of seconds before timing out
        :param xpath: XPATH of an element
        :param attribute: Name of an attribute of the element
        :param ignored_exceptions: Tuple of ignored exceptions or one ignored exception

        :return: str
        """
        driver = self.__targeted_driver
        return get_element_attribute(
            driver,
            timeout,
            xpath,
            attribute,
            ignored_exceptions=ignored_exceptions
        )

    def get_element(
            self,
            timeout: float,
            xpath: XPATH,
            ignored_exceptions: Optional[IgnoredExceptions] = None
    ) -> WebElement:
        """
        Gets element in browser
        :param timeout: Number of seconds before timing out
        :param xpath: XPATH of an element
        :param ignored_exceptions: Tuple of ignored exceptions or one ignored exception

        :return: WebElement
        """
        driver = self.__targeted_driver
        return get_element(driver, timeout, xpath, ignored_exceptions=ignored_exceptions)

    def get_elements(
            self,
            timeout: float,
            xpath: XPATH,
            ignored_exceptions: Optional[IgnoredExceptions] = None
    ) -> list[WebElement]:
        """
        Gets elements in browser
        :param timeout: Number of seconds before timing out
        :param xpath: XPATH of an element
        :param ignored_exceptions: Tuple of ignored exceptions or one ignored exception

        :return: list[WebElement]
        """
        driver = self.__targeted_driver
        return get_elements(driver, timeout, xpath, ignored_exceptions=ignored_exceptions)

    def wait_for_invisibility(
            self,
            timeout: float,
            xpath: XPATH,
            ignored_exceptions: Optional[IgnoredExceptions] = None
    ) -> None:
        """
        Wait for element's invisibility in browser
        :param timeout: Number of seconds before timing out
        :param xpath: XPATH of an element
        :param ignored_exceptions: Tuple of ignored exceptions or one ignored exception

        :return: None
        """
        driver = self.__targeted_driver
        wait_for_invisibility(driver, timeout, xpath, ignored_exceptions=ignored_exceptions)

    def wait_for_windows(
            self,
            timeout: float,
            number: int,
            *,
            ignored_exceptions: Optional[IgnoredExceptions] = None
    ) -> None:
        """
        Wait for occurring of number of windows
        :param timeout: Number of seconds before timing out
        :param number: Number of windows to be waited
        :param ignored_exceptions: Tuple of ignored exceptions or one ignoring exception

        :return: None
        """
        driver = self.__targeted_driver

        wait_for_windows(driver, timeout, number, ignored_exceptions=ignored_exceptions)

    def close_tabs(self) -> None:
        """
        Closes all tabs in browser

        :return: None
        """
        driver = self.__targeted_driver
        close_tabs(driver)
