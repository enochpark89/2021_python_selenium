from math import ceil
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

BROWSER_HEIGHT = 1027

# Create a browser variable and initiate the Chrome browser.
browser = webdriver.Chrome(ChromeDriverManager().install())

# GET request to nomadcoder.com
browser.get("https://nomadcoders.co")

# Maximize a window.
browser.maximize_window()

sizes = [
 480, 960, 1366, 1920
]


for size in sizes:
    # Change the windows size every 3 seconds.
    browser.set_window_size(size, 1027)
    time.sleep(3)

    # total scroll size gets returned after the script gets the total height on the browser. 
    scroll_size = browser.execute_script("return document.body.scrollHeight")


    # Calculate how much to scroll down.
    total_sections = ceil(scroll_size / BROWSER_HEIGHT)
    for section in range(total_sections):   
        # 
        browser.execute_script(f"window.scrollTo(0, {(section+1) * BROWSER_HEIGHT})")
        time.sleep(2)