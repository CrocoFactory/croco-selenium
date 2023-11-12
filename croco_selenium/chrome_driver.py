from typing import Optional, Iterable
from selenium.webdriver.chrome.webdriver import Options
from ._croco_driver import CrocoDriver
from .types import Proxy
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

__all__ = ['ChromeDriver']


class ChromeDriver(CrocoDriver):
    """
    The class derived from ActionPerformer, therefore it has possibility to perform actions, such as clicking, sending
    keys etc.
    """
    def __init__(
            self,
            options: Options = Options(),
            proxy: Optional[Proxy] = None,
            extension_paths: Optional[Iterable[str]] = None,
            executable_path: Optional[str] = None
    ):
        """
        :param options: This takes an instance of ChromiumOptions
        :param proxy: A proxy to be set
        :param extension_paths: An iterable collection of extension paths
        :param executable_path: An executable path of Chrome
        """
        super().__init__(
            DesiredCapabilities.CHROME["browserName"],
            "goog",
            options,
            proxy,
            extension_paths,
            executable_path
        )
