"""
croco-selenium
~~~~~~~~~~~~~~
The package providing ways to interact with Selenium Web Driver actions, such as clicking, sending keys etc.
Author's github - https://github.com/blnkoff

Usage example of actions:
   >>> from selenium.webdriver.chrome.webdriver import WebDriver
   >>> from croco_selenium import click
   >>> driver = WebDriver()
   >>> click(driver, 10, '//input[@type="submit"]')

Usage example of ActionPerformer:
   >>> from selenium.webdriver.chrome.webdriver import WebDriver
   >>> from croco_selenium import ActionPerformer
   >>> driver = WebDriver()
   >>> action_performer = ActionPerformer(driver)
   >>> action_performer.click(10, '//input[@type="submit"]')

Usage example of ChromeDriver:
   >>> import os
   >>> from croco_selenium import ChromeDriver, Proxy
   >>> proxy = Proxy(host='123.89.46.72', port=8000, username='croco', password='webDriver')
   >>> project_dir = os.path.dirname(os.path.abspath(__file__))
   >>> extensions_paths = [os.path.join(project_dir, 'extensions/metamask.crx')]
   >>>
   >>> driver = ChromeDriver(proxy=proxy, extensions_paths=extensions_paths)
   >>> driver.get('https://github.com/blnkoff/croco-webdriver')

:copyright: (c) 2023 by Alexey
:license: MIT, see LICENSE for more details.
"""

from .actions import *
from .action_performer import ActionPerformer
from .decorators import *
from .chrome_driver import ChromeDriver
from .types import Proxy
