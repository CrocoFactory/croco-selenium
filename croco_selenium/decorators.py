from typing import Any
from functools import wraps
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


def handle_pop_up(method_type: MethodType = 'object'):
    """
    Switches to another window, performs decorated function and switches back. Pop up has to be closed after performing
    decorated function.
    :param method_type: Type of method. There are three types:
                        object - decorated function has to have driver as first positional argument.
                        static - decorated function has to be @staticmethod and have driver as first positional argument
                        class - decorated function has to be @classmethod and have driver as first positional argument
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if method_type == 'object':
                driver = args[0].driver
            elif method_type == 'static':
                driver = args[0]
            elif method_type == 'class':
                driver = args[1]
            else:
                raise InvalidMethodType(method_type)

            original_window_handle = driver.current_window_handle
            current_handles = driver.window_handles
            WebDriverWait(driver, 100).until(EC.new_window_is_opened(current_handles))

            switch_to_another_window(driver)
            result = func(*args, **kwargs)

            WebDriverWait(driver, 100).until(EC.number_of_windows_to_be(len(current_handles) - 1))
            driver.switch_to.window(original_window_handle)
            return result

        return wrapper

    return decorator


def handle_in_new_tab(method_type: MethodType = 'object'):
    """
    Opens new tab, performs decorated function, closes new tab and switches back
    :param method_type: Type of method. There are three types:
                        object - decorated function has to have driver as first positional argument.
                        static - decorated function has to be @staticmethod and have driver as first positional argument
                        class - decorated function has to be @classmethod and have driver as first positional argument
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if method_type == 'object':
                driver = args[0].driver
            elif method_type == 'static':
                driver = args[0]
            elif method_type == 'class':
                driver = args[1]
            else:
                raise InvalidMethodType(method_type)

            current_tab = driver.current_window_handle
            driver.switch_to.new_window('tab')
            result = func(*args, **kwargs)
            driver.close()
            driver.switch_to.window(current_tab)
            return result

        return wrapper

    return decorator


def handle_new_tab(method_type: MethodType = 'object'):
    """
    Performs decorated function in new tab (new tab has to be opened after performing decorated function) and switches back. Decorated function has to open new tab by self.
    :param method_type: Type of method. There are three types:
                        object - decorated function has to have driver as first positional argument.
                        static - decorated function has to be @staticmethod and have driver as first positional argument
                        class - decorated function has to be @classmethod and have driver as first positional argument
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if method_type == 'object':
                driver = args[0].driver
            elif method_type == 'static':
                driver = args[0]
            elif method_type == 'class':
                driver = args[1]
            else:
                raise InvalidMethodType(method_type)

            original_window_handle = driver.current_window_handle
            result = func(*args, **kwargs)

            driver.close()
            driver.switch_to.window(original_window_handle)
            return result

        return wrapper

    return decorator
