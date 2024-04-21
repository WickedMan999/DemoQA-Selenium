from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Variable
baseURL = "https://demoqa.com"
endpoint = "buttons"

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")

# Create Chrome WebDriver instance
driver = webdriver.Chrome(options=chrome_options)


# Open URL
def ChromeBrowserCall(baseURL):
    driver.get(baseURL)
    time.sleep(3)


# Wait Timer
wait = WebDriverWait(driver, 20)

# Actionchain Instance
action = ActionChains(driver)


# Scroll Using Loop
def scroll():
    # Calculate the height of the webpage
    page_height = driver.execute_script("return document.body.scrollHeight")

    # Specify the number of times you want to scroll down
    scroll_count = 1

    # Specify the amount of scroll in pixels
    scroll_amount = 200

    # Scroll
    for loop in range(scroll_count):
        driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
    time.sleep(1)


# Invoke Double Click
def doubleClick():
    # Finding Double Click Button & Click Once It Became Clickable
    button_element = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@id='doubleClickBtn']")))

    # Double Click the button Using Actionchains
    action.double_click(button_element).perform()
    time.sleep(1)

    # Locate message after button is clicked
    message = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//p[@id='doubleClickMessage']")))

    # Extract message
    message_text = message.text
    print(message_text)


# Invoke Right Click
def rightClick():
    # Finding Right Click Button & Click Once It Became Clickable
    button_element = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@id='rightClickBtn']")))

    # Right Click the button Using Actionchains
    action.context_click(button_element).perform()
    time.sleep(1)

    # Locate message after button is clicked
    message = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//p[@id='rightClickMessage']")))

    # Extract message
    message_text = message.text
    print(message_text)


# Invoke Single Click
def singleClick():
    # Finding Button & Click Once It Became Clickable
    button_element = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "(//button[normalize-space()='Click Me'])[1]")))

    # Click the button
    button_element.click()
    time.sleep(1)

    # Locate message after button is clicked
    message = driver.find_element(By.XPATH, "//p[@id='dynamicClickMessage']")

    # Extract message
    message_text = message.text
    print(message_text)

    time.sleep(2)


# Close Browser
def closeBrowser():
    driver.quit()


# RUNNER
ChromeBrowserCall(f"{baseURL}/{endpoint}")
scroll()
doubleClick()
rightClick()
singleClick()
closeBrowser()
