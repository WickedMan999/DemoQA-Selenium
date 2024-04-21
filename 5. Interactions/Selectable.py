from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# BASEURL
base_url = "https://demoqa.com"
endpoint = "selectable"

# Customize Chrome Before It Opens
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")

# Opens Chrome Browser
driver = webdriver.Chrome(options=chrome_options)

# Explicit Wait Timer
wait = WebDriverWait(driver, 30)

# Create an ActionChains instance
action = ActionChains(driver)


def scrollDown():
    # Calculate the height of the webpage
    page_height = driver.execute_script("return document.body.scrollHeight")

    # Specify the number of times you want to scroll down
    scroll_count = 1

    # Specify the amount of scroll in pixels
    scroll_amount = 200

    # Scroll
    for i in range(scroll_count):
        driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
    time.sleep(1)


# Open URL
def ChromeBrowserCall(base_url):
    driver.get(base_url)
    time.sleep(3)


def selectableList():
    # Wait until the UL container is available
    wait.until(
        EC.presence_of_element_located((By.ID, 'verticalListContainer')))

    # Find all li elements
    li = driver.find_elements(
        By.XPATH, "//li[@class='mt-2 list-group-item list-group-item-action']")

    # Loop over the li's and click each one of them
    for i in li:
        i.click()

    time.sleep(2)


def selectableGrid():
    click_on_grid = driver.find_element(By.ID, "demo-tab-grid").click()

    # Wait until the grid container is available
    wait.until(EC.presence_of_element_located(
        (By.ID, 'demo-tabpane-grid')))

    # Define the row IDs
    row_ids = ['row1', 'row2', 'row3']

    # Loop over the rows
    for row_id in row_ids:
        # Find all the li's in the current row
        li_elements = driver.find_elements(
            By.XPATH, f"//*[@id='{row_id}']//li[@class='list-group-item list-group-item-action']")

        # Loop over the li's and click each one of them
        for i in li_elements:
            i.click()

    time.sleep(2)


def closeBrowser():
    driver.quit()


# RUNNER
ChromeBrowserCall(f"{base_url}/{endpoint}")
scrollDown()
selectableList()
selectableGrid()
closeBrowser()
