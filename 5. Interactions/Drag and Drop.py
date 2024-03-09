from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# BASEURL
base_url = "https://demoqa.com"
endpoint = "droppable"

# Customize Chrome Before It Opens
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")

# Opens Chrome Browser
driver = webdriver.Chrome(options=chrome_options)

# Explicit Wait Timer
wait = WebDriverWait(driver, 20)

# Create an ActionChains instance
action = ActionChains(driver)


# Open URL
def ChromeBrowserCall(base_url):
    driver.get(base_url)


# Drag and Drop
def dragDrop():
    # Locate Element To Drag
    element_to_drag = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#draggable")))

    # Locate Element To Drop
    element_to_drop = wait.until(EC.presence_of_element_located(
        (By.XPATH, "(//div[@id='droppable'])[1]")))

    # Perform Drag and Drop
    action.drag_and_drop(element_to_drag, element_to_drop).perform()
    time.sleep(3)


# Close Browser
def closeBrowser():
    driver.quit()


# RUNNER
ChromeBrowserCall(f"{base_url}/{endpoint}")
dragDrop()
closeBrowser()
