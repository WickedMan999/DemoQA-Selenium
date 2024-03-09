from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# BASEURL
base_url = "https://demoqa.com"
endpoint = "dragabble"

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


def scrollDown(scroll_amount):
    # Calculate the height of the webpage
    page_height = driver.execute_script("return document.body.scrollHeight")

    # Specify the number of times you want to scroll down
    scroll_count = 1

    # Specify the amount of scroll in pixels
    scroll_amount = scroll_amount

    # Scroll
    for i in range(scroll_count):
        driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
    time.sleep(1)


# Open URL
def ChromeBrowserCall(base_url):
    driver.get(base_url)


def simpleDrag():
    element_to_drag = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#dragBox")))

    # Click & hold element, move by x & y axis, release element, perform this actionchain
    action.click_and_hold(element_to_drag).move_by_offset(
        200, 500).release().perform()

    time.sleep(2)

# NOTE: IF the area is not visible it will throw error


def dragAndDropAxis():
    # Click on Axis Restricted
    button = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#draggableExample-tab-axisRestriction"))).click()

    # X-Axis - Horizontal
    element_to_drag_x = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#restrictedX")))

    # Loop for 2 times
    for i in range(2):
        # Move 50 pixels Right Using Actionchains
        action.click_and_hold(element_to_drag_x).move_by_offset(
            200, 0).release().perform()

        time.sleep(1)

        # Move 50 pixels Left Using Actionchains
        action.click_and_hold(element_to_drag_x).move_by_offset(
            -200, 0).release().perform()

        time.sleep(1)

    # Y-Axis - Vertically
    element_to_drag_y = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#restrictedY")))

    # Loop for 2 times
    for i in range(2):
        # Move 50 pixels up Using Actionchains
        action.click_and_hold(element_to_drag_y).move_by_offset(
            0, -80).release().perform()

        time.sleep(1)

        # Move 50 pixels down Using Actionchains
        action.click_and_hold(element_to_drag_y).move_by_offset(
            0, 80).release().perform()

        time.sleep(1)

    time.sleep(2)


# Close Browser
def closeBrowser():
    driver.quit()


# RUNNER
ChromeBrowserCall(f"{base_url}/{endpoint}")
scrollDown(400)
simpleDrag()
scrollDown(-800)
dragAndDropAxis()
closeBrowser()
