from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# BASEURL
base_url = "https://demoqa.com"
endpoint = "alerts"

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


# Scroll down of webpage using Loop
def scrollDown():
    # Specify the number of times you want to scroll down
    scroll_count = 1

    # Specify the amount of scroll in pixels
    scroll_amount = 200

    # Scroll
    for i in range(scroll_count):
        driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
    time.sleep(1)


# Simple Alert with OK button
def alertButton():
    alert_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@id='alertButton']"))
    )
    alert_button.click()

    # Switch to alert popup
    alert_popup = driver.switch_to.alert

    # Print message from popup
    alert_text = alert_popup.text
    print("Alert Message 1 :", alert_text)

    # Accept alert
    alert_popup.accept()

    time.sleep(1)


# Alert popup displayed after 5 sec
def timerAlertButton():
    try:
        alert_button = driver.find_element(
            By.XPATH, "(//button[@id='timerAlertButton'])[1]")
        alert_button.click()

        # Wait for 5 sec until the alert to be present
        alert_popup = wait.until(EC.alert_is_present())

        # Print text from popup
        alert_text = alert_popup.text
        print("Alert Message 2 :", alert_text)

        # Accept alert
        alert_popup.accept()

        time.sleep(2)

    except TimeoutException:
        print("No alert appeared within the given time frame")


# Alert with Ok and Cancel Button
def confirmAlertButton():
    alert_button = driver.find_element(
        By.XPATH, "//button[@id='confirmButton']")
    alert_button.click()

    # Switch to alert popup
    alert_popup = driver.switch_to.alert

    # Print text from popup
    alert_text = alert_popup.text
    print("Alert Text 3 :", alert_text)

    # Accept Alert
    alert_popup.accept()

    time.sleep(2)


def promptAlertButton():
    # Element
    alert_button = driver.find_element(
        By.XPATH, "//button[@id='promtButton']")
    alert_button.click()

    # Switch to the alert
    alert = driver.switch_to.alert

    # Type something in the prompt box
    alert.send_keys("This is Wicked Man")

    # Print the text in the alert box
    print(alert.text)

    # Accept the alert box
    alert.accept()

    # Typed name
    typed_letter = driver.find_element(By.XPATH, "//span[@id='promptResult']")
    print(typed_letter.text)

    time.sleep(2)


# Close Browser
def closeBrowser():
    driver.quit()


# Runner
ChromeBrowserCall(f"{base_url}/{endpoint}")
scrollDown()
alertButton()
timerAlertButton()
confirmAlertButton()
promptAlertButton()
closeBrowser()
