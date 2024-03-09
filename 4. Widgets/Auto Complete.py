from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# BASEURL
base_url = "https://demoqa.com"
endpoint = "auto-complete"

# Customize Chrome Before It Opens
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")

# Opens Chrome Browser
driver = webdriver.Chrome(options=chrome_options)

# Explicit Wait Timer
wait = WebDriverWait(driver, 30)

# ActionChain Instance
actions = ActionChains(driver)


# Open URL
def ChromeBrowserCall(base_url):
    driver.get(base_url)


def autoCompleteMultipleColor():
    # Locating Element Using Explicit Wait
    element = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@id='autoCompleteMultipleContainer']")))

    # Colors to select
    colors_to_select = ['Red', 'Blue', 'Green', 'Yellow']

    for color in colors_to_select:  # It will select all colors
        # Move to 'element' 'click' on element' & perform
        actions.move_to_element(element).click().perform()

        # Clear 'Move to element & click' action & perform new action i.e. 'send key:red' on 2nd loop it will 'send key:blue'
        for i in color:
            actions.send_keys(i).perform()
            actions.reset_actions()  # Reset the actions queue

        # Clear 'send key:red' action & perform new action i.e. 'send key:arrow down'
        actions.reset_actions()  # Reset the actions queue
        actions.send_keys(Keys.ARROW_DOWN).perform()

        # Clear 'send key:arrrow down' action & perform new action i.e. 'send key:return/enter'
        actions.reset_actions()  # Reset the actions queue
        actions.send_keys(Keys.ENTER).perform()

        # Print and confirm the selected color
        print(f"Selected color on Multiple Color: {color}")

    time.sleep(2)


def autoCompleteSingleColor():
    # Locating Element Using Explicit Wait
    element = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="autoCompleteSingleContainer"]')))

    # Move to 'element' 'click' on element' & perform
    actions.move_to_element(element).click().perform()

    # Clear 'Move to element & click' action & perform new action i.e. 'send key:red' on 2nd loop it will 'send key:blue'
    actions.reset_actions()  # Reset the actions queue
    actions.send_keys("Red").perform()

    # Clear 'send key:red' action & perform new action i.e. 'send key:arrow down'
    actions.reset_actions()  # Reset the actions queue
    actions.send_keys(Keys.ARROW_DOWN).perform()

    # Clear 'send key:arrrow down' action & perform new action i.e. 'send key:return/enter'
    actions.reset_actions()  # Reset the actions queue
    actions.send_keys(Keys.ENTER).perform()

    # Print and confirm the selected color
    print(f"Selected color on Single Color: Red")

    time.sleep(1)


# Close Browser
def closeBrowser():
    driver.quit()


ChromeBrowserCall(f"{base_url}/{endpoint}")
autoCompleteMultipleColor()
autoCompleteSingleColor()
closeBrowser()
