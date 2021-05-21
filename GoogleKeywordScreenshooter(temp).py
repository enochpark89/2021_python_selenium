from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

KEYWORD = "buy domain"

# install Chrome Driver Manager and launch Crhome
browser = webdriver.Chrome(ChromeDriverManager().install())

# Type send GET request to google.com
browser.get("https://google.com")

search_bar = browser.find_element_by_class_name("gLFyf")

# Write Hello under a input element.
search_bar.send_keys(KEYWORD)
# Press ENTER key
search_bar.send_keys(Keys.ENTER)
# Get all the elements of the search results
search_results = browser.find_elements_by_class_name("g")

# loop through the search results and extract h3 elements only.

"""
for search_result in search_results:
    title = search_result.find_element_by_tag_name("h3")
    if title:
        print(title.text)

for index, search_result in enumerate(search_results):
    class_name = search_result.get_attribute("class")
    print(class_name)
    if "kno-kp mnr-c g-blk" not in class_name:
        search_result.screenshot(f"screenshots/{KEYWORD}x{index}.png")
"""

shitty_element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "g-blk"))
)

# execute script with an stated argument. This script will remove the unnecessary elements.
browser.execute_script(
    """
const shitty = arguments[0];
shitty.parentElement.removeChild(shitty)
""",
    shitty_element,
)
# browser.quit()
