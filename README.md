# Selenium

-  App that automatte Web tasks.

# Overview

Composed of three apps:

1. Google Scrapping
2. Responsive Tester
3. Instamming

# Requirement

1. Virtuallenwrapper: work with dependencies in python (alt. pipenv, poetry)
   _Since Virtualenwrapper did not work on my Windows, I used pipen_
2. Selenium: Install Selenium > _pip install selenium_
3. ChromeDriver: Install ; Install package called 'webdriver*manager' so that this may manage the package versions.; Use \_pip install webdriver_manager*

# DevProgress

# 1.0 Google Scrapping

## 1.0a Start a driver

-  Use below code to execute Chrome browser within the python.

```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
# The virtual Chrome browser will open from Python.
```

## 1.0b Search

-  We found **Web element**.
-  There elements are found on the web pages.
-  There are many functions that you can use to find elements. (Please read the selenium documentation).
   -  submit, id, screenshot_as_png etc.
-  In order to search, you need to find an element that takes in the search input.

```python
search_bar = browser.find_element_by_class_name("gLFyf")
print(search_bar)

browser.quit()
"""
Output:
<selenium.webdriver.remote.webelement.WebElement (session="cbae19a6d58bb6ab1c385fc1a7b579eb", element="852f99fe-2005-4679-8c2e-2ea86011743c")>
"""
```

-  Since it finds the input element, you can make selenium type the value inside the input.
   -  Use send_keys()

```python
search_bar.send_keys("hello!")
```

-  You can make the chrome browser press enter using selenium.webdriver.common.keys (Please look at the Web Driver API of Selenium Docs: https://selenium-python.readthedocs.io/api.html)

-  After you press the enter, you can tell the browser to grab all the elements of the serach results.

main.py:

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# install Chrome Driver Manager and launch Crhome
browser = webdriver.Chrome(ChromeDriverManager().install())

# Type send GET request to google.com
browser.get("https://google.com")

search_bar = browser.find_element_by_class_name("gLFyf")

# Write Hello under a input element.
search_bar.send_keys("hello!")
# Press ENTER key
search_bar.send_keys(Keys.ENTER)
# Get all the elements of the search results
search_results = browser.find_elements_by_class_name("g")

print(search_results)

```

## 1.0c Finding results

-  **Web element**: Web elements are elements found in the webpage.

-  you can find all the titles of the search result.
-  you scrape the h3 element using the below code:

```python
for search_result in search_results:
    title = search_result.find_element_by_tag_name("h3")
    if title:
        print(title.text)
```

-  find_element: find the first class
-  find_elements: find many elements.
-  you used h3 because you noticed that the serach results provide title within the h3 elements.

## 1.0d Screenshots

-  you can make the browser take the screenshot.
-  we need to exclude some textboxes that are in the middle that starts with "g"
-  Use .getAtrribute();
-  manually remove some elements that might bother the screenshot.
-  if you want to wait for a browser to load, you can use the expected_conditions. You have to wait for the JS to load and then, you want to remove the unnecessary elements.

```python
# New imports:
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

shitty_element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "g-blk"))
)

print(shitty_element)
# Output:
"""
<selenium.webdriver.remote.webelement.WebElement (session="77b2f69fa2a93ecdaf9ed9a87af33616", element="30812992-267c-4fa5-a45a-eb101dd48b14")>
"""
```

## 1.0e Send JS from Python

-  you can remove the element using the JavaScript
   Steps:

1. Find an element.
2. Find a father.
3. Remove a child.

Sending JS script to python.

```python
# execute JS script with an stated argument. This script will remove the unnecessary elements.
browser.execute_script(
"""
const shitty = argument[0];
shitty.parentElement.removeChild(shitty)
""",
    shitty_element,
  )
```

-  Once you remove unnecessary elements, you can take the screenshots.

**Recap**:

-  We learn that we can control the browser.
-  Every code gets sent to the browser.
-  You can use package keys to make the robot press enter within the browser.
-  We can send the JS script from the Python to the browser.
-  You always write the code first and make it better later.
-  The improvement would be making the script-like funciton into OOP-like codes with classes.

# 2.0 Responsive Tester

-  You can resize the windows. There are many standard sizes shown on the website Microsoft.

-  Current height:
   {'width': 1552, 'height': 840}

-  Make the Chrome browser window resize every 5 seconds.

```python
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Create a browser variable and initiate the Chrome browser.
browser = webdriver.Chrome(ChromeDriverManager().install())

# GET request to nomadcoder.com
browser.get("https://nomadcoders.co")

# Maximize a window.
browser.maximize_window()

sizes = [
    320, 480, 960, 1366, 1920
]

# Change the windows size every 5 seconds.
for size in sizes:
    browser.set_window_size(size, 1027)
    time.sleep(5)

```

# 2.0a Scroll down.

- We need to figure out the total scroll height. (body.scroll.height())
- You can use the Javascript script to execute the dommand. 
- You can also send the JavaScript send information back to the Python. 
- If you divide the browser height from the scroll_size, you get how much you can scroll down. 
- range() gives an array of how much you are going to give it. 
- Each scroll down will be the browser height. 

# Instamining 

- We are going to take one hash tag and take all the related hashtags and count how many posts that they have. 
