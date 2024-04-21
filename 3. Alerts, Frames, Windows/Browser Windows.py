from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# BASEURL
base_url = "https://demoqa.com"
endpoint = "browser-windows"

# Customize Chrome Before It Opens
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")

# Opens Chrome Browser
driver = webdriver.Chrome(options=chrome_options)

# Explicit Wait Timer
wait = WebDriverWait(driver, 10)


# Open URL
def ChromeBrowserCall(base_url):
    driver.get(base_url)
    time.sleep(3)


# Handle New Tab
def handleNewTab():
    # Find button element that opens tab
    new_tab = driver.find_element(By.XPATH, "//button[@id='tabButton']")

    # Save this tab as default tab | Index 0
    default_tab = driver.current_window_handle

    # Click to open new tab
    new_tab.click()
    time.sleep(2)

    # Save this tab as new tab | Index 1
    new_tab = driver.window_handles[1]

    # Switch back to the default tab
    driver.switch_to.window(default_tab)
    time.sleep(2)

    # Switch back to the new tab by index
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)

    # Close new tab
    driver.close()

    time.sleep(4)


# Handle New Windows
def handleNewWindows():
    # Find button element that opens new windows
    new_window = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//button[@id='windowButton']")))

    # Save this window as default window | Index 0
    default_window = driver.window_handles[0]

    # Click to open new Window
    new_window.click()
    time.sleep(2)

    # Save newly opened window as new window | Index 1
    new_window = driver.window_handles[1]

    # Switch to the new window
    driver.switch_to.window(new_window)

    # Switch back to the original window
    driver.switch_to.window(default_window)
    time.sleep(2)

    # Switch to the new window
    driver.switch_to.window(new_window)
    time.sleep(2)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com")
    time.sleep(2)

    # Close new windows
    driver.close()

    time.sleep(2)


# Close Browser
def closeBrowser():
    driver.quit()


# RUNNER
ChromeBrowserCall(f"{base_url}/{endpoint}")
# handleNewTab()
handleNewWindows()
closeBrowser()
