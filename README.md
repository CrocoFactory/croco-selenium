# croco-selenium
[![Croco Logo](https://i.ibb.co/G5Pjt6M/logo.png)](https://t.me/crocofactory)

The package providing ways to interact with Selenium Web Driver actions, such as clicking, sending keys etc.
    

- **[Telegram channel](https://t.me/crocofactory)**
- **[Bug reports](https://github.com/blnkoff/croco-selenium/issues)**
- **[Actions Overview](#actions-overview)**

When we use Selenium, it's not convenient to use WebDriverWait with its cluttered chain actions. Instead of many imports 
and instances (By, WebDriverWait, expected_conditions) you can use fast and robust actions.

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

One of the best ways to use actions is create an instance of ChromeDriver and perform 
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
You can perform the following [actions](#actions), using croco-selenium:

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

And there are 3 useful [decorators](#decorators):

- **[handle_pop_up](#handle_pop_up)**
- **[handle_in_new_tab](#handle_in_new_tab)**
- **[handle_new_tab](#handle_new_tab)**
         
## Actions

<h3 id="add_cookies">add_cookies</h3>
Adds cookies to a current page. It takes valid string containing json, list of cookies or one cookie as dictionary.

```python
from croco_selenium import ChromeDriver

timeout = 10
driver = ChromeDriver()

cookies = '{"domain":".facebook.com","expirationDate":1689249734,"httpOnly":true,"name":"c_user","path":"/","secure":true,"value":"100083466604886"}'
driver.get('facebook.com')
driver.add_cookies(cookies)
```

<h3 id="click">click</h3>
Clicks on element in browser

```python
from croco_selenium import ChromeDriver

timeout = 10
driver = ChromeDriver()
driver.click(timeout, '//input[@type="submit"]')
```

<h3 id="close_tabs">close_tabs</h3>
Closes all tabs in browser. It's convenient to use, when you add extensions to your browser and their windows occur with 
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
from croco_selenium import ChromeDriver

timeout = 10
driver = ChromeDriver()

element = driver.get_element(timeout, '//input[@type="submit"]')
element.click()
```

<h3 id="get_elements">get_elements</h3>
Returns an elements in browser

```python
from croco_selenium import ChromeDriver

timeout = 10
driver = ChromeDriver()

elements = driver.get_elements(timeout, '//input')

for element in elements:
    element.click()
```

<h3 id="get_element_attribute">get_element_attribute</h3>
Returns an element's attribute in browser

```python
from croco_selenium import ChromeDriver

timeout = 10
driver = ChromeDriver()

assert driver.get_element_attribute(timeout, '//input[@type="checkbox"]', 'checked')
```

<h3 id="get_element_text">get_element_text</h3>
Returns element's text in browser

```python
from croco_selenium import ChromeDriver

timeout = 10
driver = ChromeDriver()

print(driver.get_element_text(timeout, '//h1'))
```

<h3 id="send_keys">send_keys</h3>
Sends keys in browser

```python
from croco_selenium import ChromeDriver

timeout = 10
driver = ChromeDriver()

driver.send_keys(timeout, '//input[@type="password"]', 'password')
driver.click(timeout, '//input[@type="submit"]')
```

<h3 id="silent_send_keys">silent_send_keys</h3>
Sends keys with delay between characters in browser. It's convenient to use when you would like to hide your bot activity

```python
from croco_selenium import ChromeDriver

timeout = 10
driver = ChromeDriver()

driver.silent_send_keys(timeout, '//input[@type="password"]', 'password')
driver.click(timeout, '//input[@type="submit"]')
```

<h3 id="switch_to_another_window">switch_to_another_window</h3>
Switches to a different window from current window in browser. It's convenient to use, when you have two windows to be handled

```python
from croco_selenium import ChromeDriver

timeout = 10
driver = ChromeDriver()

driver.silent_send_keys(timeout, '//input[@type="password"]', 'password')
driver.click(timeout, '//input[@type="submit"]')
driver.switch_to_another_window(timeout)

driver.click(timeout, '//input[@type="submit"]')
driver.switch_to_another_window(timeout)
```

<h3 id="switch_to_frame">switch_to_frame</h3>
Switches to the frame

```python
from croco_selenium import ChromeDriver

timeout = 10
driver = ChromeDriver()

driver.switch_to_frame(timeout, '//iframe[@data-hcaptcha-widget-id]')
driver.click(timeout, '//input[@type="submit"]')
```

<h3 id="switch_to_parent_frame">switch_to_parent_frame</h3>
Switches to the parent frame

```python
from croco_selenium import ChromeDriver

timeout = 10
driver = ChromeDriver()

driver.switch_to_frame(timeout, '//iframe[@data-hcaptcha-widget-id]')
driver.click(timeout, '//input[@type="submit"]')
driver.switch_to_parent_frame()
```

<h3 id="wait_for_invisibility">wait_for_invisibility</h3>
Wait for element's invisibility in browser

```python
from croco_selenium import ChromeDriver

timeout = 10
driver = ChromeDriver()

driver.click(timeout, '//button')
driver.wait_for_invisibility(timeout, '//*[@id="popup"]')
```
      
<h3 id="wait_for_windows">wait_for_windows</h3>
Wait for occurring of number of windows

```python
from croco_selenium import ChromeDriver

timeout = 10
driver = ChromeDriver()

driver.wait_for_windows(timeout, 2)
```

## Decorators
<h3 id="handle_pop_up">handle_pop_up</h3>
Switches to another window, performs decorated function and switches back. Pop up has to be closed after performing
decorated function.

This decorator is usually used for browser extensions' pop-ups. Example of function performing
a third-party Metamask connection:

```python
from croco_selenium import ChromeDriver, handle_pop_up
from selenium.common import TimeoutException

@handle_pop_up()
def connect(driver: ChromeDriver, password: str) -> None:
    try:
        password_xpath = '//*[@id="password"]'
        driver.send_keys(7, password_xpath, password)

        unlock_xpath = '//button[@data-testid="unlock-submit"]'
        driver.click(5, unlock_xpath)
    except TimeoutException:
        pass

    for _ in range(3):
        next_xpath = '//button[@data-testid="page-container-footer-next"]'
        driver.click(10, next_xpath, ignored_exceptions=TimeoutException)
```

<h3 id="handle_in_new_tab">handle_in_new_tab</h3>
Opens new tab, performs decorated function, closes new tab and switches back. Here is example of function performing 
getting of 2FA code from browser extension.

```python
from croco_selenium import ChromeDriver, handle_in_new_tab

@handle_in_new_tab()
def get_code(driver: ChromeDriver, account) -> str:
    timeout = 15

    driver.get('<EXTENSION_URL>')

    code_field_xpath = '//*[contains(@class, "code")]'
    code_fields = driver.get_elements(timeout, code_field_xpath)

    code_field = code_fields[account.id]

    code = code_field.text
    return code
```

<h3 id="handle_new_tab">handle_new_tab</h3>
Performs decorated function in new tab and switches back. New tab has to be opened during performing decorated function.


# Installing croco-selenium

To install the package from PyPi you can use:   

```sh
pip install croco-selenium
```
   
To install the package from GitHub you can use:

```sh
pip install git+https://github.com/blnkoff/croco-selenium.git
```