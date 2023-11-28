# croco-selenium-actions
[![Croco Logo](https://i.ibb.co/G5Pjt6M/logo.png)](https://t.me/crocofactory)

The package providing ways to interact with Selenium Web Driver actions, such as clicking, sending keys etc.
    

- **[Telegram channel](https://t.me/crocofactory)**
- **[Bug reports](https://github.com/blnkoff/republik-warmer/issues)**
- **[Actions Overview](#actions-overview)**

Package's source code is made available under the [MIT License](LICENSE)

# Quick Start
     
You can use actions, by the following way.

```python
from selenium.webdriver.chrome.webdriver import WebDriver
from croco_selenium import click
driver = WebDriver()
click(driver, 10, '//input[@type="submit"]')
```

If you don't want to pass driver every using of actions, you can create an instance of ActionPerformer

```python
from selenium.webdriver.chrome.webdriver import WebDriver
from croco_selenium import ActionPerformer
driver = WebDriver()
action_performer = ActionPerformer(driver)
timeout = 10

action_performer.send_keys(timeout, '//input[@type="password"]', 'password')
action_performer.click(timeout, '//input[@type="submit"]')
```

If you don't use anti-detect browsers, the best way to use actions is create an instance of ChromeDriver and perform 
actions by calling methods on it. That class derived from ActionPerformer and ChromiumDriver

```python
import os
from croco_selenium import ChromeDriver, Proxy
proxy = Proxy(host='123.89.46.72', port=8000, username='croco', password='webDriver')
project_dir = os.path.dirname(os.path.abspath(__file__))
extension_paths = [os.path.join(project_dir, 'extensions/metamask.crx')]

driver = ChromeDriver(proxy=proxy, extension_paths=extension_paths)
driver.get('https://facebook.com')
driver.send_keys(15, '//input[@id="email"]', 'hello@world.com')
```

# Actions Overview
You can perform the following actions, using croco-selenium:

- **[add_cookies](#add_cookies)**
- **[click](#click)**
- **[close_tabs](#close_tabs)**
- **[get_element](#get_element)**
- **[get_elements](#get_elements)**
- **[get_element_attribute](#get_element_attribute)**
- **[get_element_text](#get_element_text)**
- **[send_keys](#send_keys)**
- **[silent_send_keys](#silent_send_keys)**
- **[switch_to_another_window](#switch_to_another_window)**
- **[switch_to_frame](#switch_to_frame)**
- **[switch_to_parent_frame](#switch_to_parent_frame)**
- **[wait_for_invisibility](#wait_for_invisibility)**
- **[wait_for_windows](#wait_for_windows)**

<h3 id="add_cookies">add_cookies</h3>
Adds cookies to a current page. It takes valid string containing json, list of cookies or one cookie as dictionary.

```python
from selenium.webdriver.chrome.webdriver import WebDriver
from croco_selenium import ActionPerformer
driver = WebDriver()
action_performer = ActionPerformer(driver)
timeout = 10

cookies = '{"domain":".facebook.com","expirationDate":1689249734,"httpOnly":true,"name":"c_user","path":"/","secure":true,"value":"100083466604886"}'

action_performer.add_cookies(cookies)
```

<h3 id="click">click</h3>
Clicks on element in browser

```python
from selenium.webdriver.chrome.webdriver import WebDriver
from croco_selenium import ActionPerformer
driver = WebDriver()
action_performer = ActionPerformer(driver)
timeout = 10

action_performer.click(timeout, '//input[@type="submit"]')
```

<h3 id="close_tabs">close_tabs</h3>
Closes all tabs in browser. It's convenient to use, when you add extensions to your browser and their windows occure with 
starting a driver.

```python
import os
from croco_selenium import ChromeDriver

project_dir = os.path.dirname(os.path.abspath(__file__))
extension_paths = [os.path.join(project_dir, 'extensions/metamask.crx')]

driver = ChromeDriver(extension_paths=extension_paths)
driver.close_tabs()
driver.get('https://facebook.com')
driver.send_keys(15, '//input[@id="email"]', 'hello@world.com')
```

<h3 id="get_element">get_element</h3>
Returns an element in browser

```python
from selenium.webdriver.chrome.webdriver import WebDriver
from croco_selenium import ActionPerformer
driver = WebDriver()
action_performer = ActionPerformer(driver)
timeout = 10

action_performer.get_element(timeout, '//input[@type="submit"]')
```

<h3 id="get_elements">get_elements</h3>
Returns an elements in browser

```python
from selenium.webdriver.chrome.webdriver import WebDriver
from croco_selenium import ActionPerformer
driver = WebDriver()
action_performer = ActionPerformer(driver)
timeout = 10

action_performer.get_elements(timeout, '//input')
```

<h3 id="get_element_attribute">get_element_attribute</h3>
Returns an element's attribute in browser

```python
from selenium.webdriver.chrome.webdriver import WebDriver
from croco_selenium import ActionPerformer
driver = WebDriver()
action_performer = ActionPerformer(driver)
timeout = 10

assert action_performer.get_element_attribute(timeout, '//input[@type="checkbox"]', 'checked')
```

<h3 id="get_element_text">get_element_text</h3>
Returns element's text in browser

```python
from selenium.webdriver.chrome.webdriver import WebDriver
from croco_selenium import ActionPerformer
driver = WebDriver()
action_performer = ActionPerformer(driver)
timeout = 10

print(action_performer.get_element_text(timeout, '//h1'))
```

<h3 id="send_keys">send_keys</h3>
Sends keys in browser

```python
from selenium.webdriver.chrome.webdriver import WebDriver
from croco_selenium import ActionPerformer
driver = WebDriver()
action_performer = ActionPerformer(driver)
timeout = 10

action_performer.send_keys(timeout, '//input[@type="password"]', 'password')
action_performer.click(timeout, '//input[@type="submit"]')
```

<h3 id="silent_send_keys">silent_send_keys</h3>
Sends keys with delay between characters in browser. It's convenient to use when you would like to hide your bot activity

```python
from selenium.webdriver.chrome.webdriver import WebDriver
from croco_selenium import ActionPerformer
driver = WebDriver()
action_performer = ActionPerformer(driver)
timeout = 10

action_performer.silent_send_keys(timeout, '//input[@type="password"]', 'password')
action_performer.click(timeout, '//input[@type="submit"]')
```

<h3 id="switch_to_another_window">switch_to_another_window</h3>
Switches to a different window from current window in browser. It's convenient to use, when you have two windows to be handled

```python
from selenium.webdriver.chrome.webdriver import WebDriver
from croco_selenium import ActionPerformer
driver = WebDriver()
action_performer = ActionPerformer(driver)
timeout = 10

action_performer.silent_send_keys(timeout, '//input[@type="password"]', 'password')
action_performer.click(timeout, '//input[@type="submit"]')
action_performer.switch_to_another_window(timeout)

action_performer.click(timeout, '//input[@type="submit"]')
action_performer.switch_to_another_window(timeout)
```

<h3 id="switch_to_frame">switch_to_frame</h3>
Switches to the frame

```python
from selenium.webdriver.chrome.webdriver import WebDriver
from croco_selenium import ActionPerformer
driver = WebDriver()
action_performer = ActionPerformer(driver)
timeout = 10

action_performer.switch_to_frame(timeout, '//iframe[@data-hcaptcha-widget-id]')
action_performer.click(timeout, '//input[@type="submit"]')
```

<h3 id="switch_to_parent_frame">switch_to_parent_frame</h3>
Switches to the parent frame

```python
from selenium.webdriver.chrome.webdriver import WebDriver
from croco_selenium import ActionPerformer
driver = WebDriver()
action_performer = ActionPerformer(driver)
timeout = 10

action_performer.switch_to_frame(timeout, '//iframe[@data-hcaptcha-widget-id]')
action_performer.click(timeout, '//input[@type="submit"]')
action_performer.switch_to_parent_frame()
```

<h3 id="wait_for_invisibility">wait_for_invisibility</h3>
Wait for element's invisibility in browser

```python
from selenium.webdriver.chrome.webdriver import WebDriver
from croco_selenium import ActionPerformer
driver = WebDriver()
action_performer = ActionPerformer(driver)
timeout = 10

action_performer.click(timeout, '//button')
action_performer.wait_for_invisibility(timeout, '//*[@id="popup"]')
```
      
<h3 id="wait_for_windows">wait_for_windows</h3>
Wait for occurring of number of windows

```python
from selenium.webdriver.chrome.webdriver import WebDriver
from croco_selenium import ActionPerformer
driver = WebDriver()
action_performer = ActionPerformer(driver)
timeout = 10

action_performer.wait_for_windows(timeout, 2)
```

# Installing croco-selenium-actions

To install the package from GitHub you can use:

```sh
pip install git+https://github.com/blnkoff/croco-selenium-actions.git
```