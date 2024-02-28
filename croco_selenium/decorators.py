from functools import wraps
from typing import Callable
from selenium.webdriver.chrome.webdriver import WebDriver
from .exceptions import InvalidMethodType
from .actions import switch_to_another_window
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .types import MethodType

__all__ = [
    'handle_pop_up',
    'handle_new_tab',
    'handle_in_new_tab'
]


def _get_driver(method_type: MethodType, *args) -> WebDriver:
    if method_type == 'instance':
        driver = args[0].driver
    elif method_type in ['static', 'function']:
        driver = args[0]
    elif method_type == 'class':
        driver = args[1]
    elif method_type == 'function':
        driver = args[0]
    else:
        raise InvalidMethodType(method_type)

    return driver


def handle_pop_up(func: Callable = None, *, method_type: MethodType = 'instance'):
    """
    Switches to another window, performs decorated function and switches back. Pop up has to be closed after performing
    decorated function.
    :param func: Function to be decorated
    :param method_type: Type of method. There are three types:
                        instance - decorated function has to be instance-method and have attribute 'driver' in `self` namespace
                        static, function - decorated function has to have driver as first positional argument
                        class - decorated function has to be @classmethod and have attribute driver in 'cls' namespace
    """
    if not callable(func):
        return lambda f: handle_pop_up(f, method_type=method_type)

    @wraps(func)
    def wrapper(*args, **kwargs):
        driver = _get_driver(method_type, *args)

        original_window_handle = driver.current_window_handle
        current_handles = driver.window_handles
        WebDriverWait(driver, 100).until(EC.new_window_is_opened(current_handles))
        current_handles = driver.window_handles

        switch_to_another_window(driver)
        result = func(*args, **kwargs)

        WebDriverWait(driver, 100).until(EC.number_of_windows_to_be(len(current_handles) - 1))
        driver.switch_to.window(original_window_handle)
        return result

    return wrapper


def handle_in_new_tab(func: Callable = None, method_type: MethodType = 'instance'):
    """
    Opens new tab, performs decorated function, closes new tab and switches back
    :param func: Function to be decorated
    :param method_type: Type of method. There are three types:
                        instance - decorated function has to be instance-method and have attribute 'driver' in `self` namespace
                        static, function - decorated function has to have driver as first positional argument
                        class - decorated function has to be @classmethod and have attribute driver in 'cls' namespace
    """

    if not callable(func):
        return lambda f: handle_in_new_tab(f, method_type=method_type)

    @wraps(func)
    def wrapper(*args, **kwargs):
        driver = _get_driver(method_type, *args)

        current_tab = driver.current_window_handle
        driver.switch_to.new_window('tab')
        result = func(*args, **kwargs)
        driver.close()
        driver.switch_to.window(current_tab)
        return result

    return wrapper


def handle_new_tab(func: Callable = None, method_type: MethodType = 'instance'):
    """
    Performs decorated function in new tab (new tab has to be opened after performing decorated function) and switches back. 
    Decorated function has to open new tab by self.
    :param func: Function to be decorated
    :param method_type: Type of method. There are three types:
                        instance - decorated function has to be instance-method and have attribute 'driver' in `self` namespace
                        static, function - decorated function has to have driver as first positional argument
                        class - decorated function has to be @classmethod and have attribute driver in 'cls' namespace
    """
    if not callable(func):
        return lambda f: handle_in_new_tab(f, method_type=method_type)

    @wraps(func)
    def wrapper(*args, **kwargs):
        driver = _get_driver(method_type, *args)

        original_window_handle = driver.current_window_handle
        result = func(*args, **kwargs)

        driver.close()
        driver.switch_to.window(original_window_handle)
        return result

    return wrapper
