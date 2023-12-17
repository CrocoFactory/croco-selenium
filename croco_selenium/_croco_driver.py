from typing import Optional, Iterable
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.chromium.webdriver import ChromiumDriver
from .types import Proxy
from .action_performer import ActionPerformer


class CrocoDriver(ChromiumDriver, ActionPerformer):
    def __init__(
            self,
            browser_name: str,
            vendor_prefix: str,
            options: ChromiumOptions = ChromiumOptions(),
            proxy: Optional[Proxy] = None,
            extension_paths: Optional[Iterable[str]] = None,
            executable_path: Optional[str] = None
    ):
        if extension_paths:
            for path in extension_paths:
                options.add_extension(path)

        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("--start-maximized")

        if proxy:
            options.add_argument(f'--proxy-server={proxy["host"]}:{proxy["port"]}')
            options.add_argument(f'--proxy-auth={proxy["username"]}:{proxy["password"]}')

        service = ChromiumService(executable_path=executable_path) if executable_path else ChromiumService()

        ChromiumDriver.__init__(self, browser_name, vendor_prefix, options, service)
        ActionPerformer.__init__(self, self)
