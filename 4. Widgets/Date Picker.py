from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


# BASEURL
base_url = "https://demoqa.com"
endpoint = "date-picker"

# Customize Chrome Before It Opens
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")

# Opens Chrome Browser
driver = webdriver.Chrome(options=chrome_options)

# Explicit Wait Timer
wait = WebDriverWait(driver, 30)


# Open URL
def ChromeBrowserCall(base_url):
    driver.get(base_url)
    time.sleep(3)


# Date Picker using JavaScript
def datePicker():
    try:
        # Locating Element Using Explicit Wait
        date = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#datePickerMonthYearInput")))

        # Invoke JS to select date
        driver.execute_script(
            "arguments[0].value = '04/18/1999';", date)

    except Exception as e:
        print("An error occurred:", e)
    time.sleep(2)


# Date Picker using JavaScript
def dateAndTimePicker():
    # Locating Element Using Explicit Wait
    date_and_time = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#dateAndTimePickerInput")))

    # Invoke JS to select date and time
    driver.execute_script(
        "arguments[0].value = 'December 11, 2020 12:12 AM';", date_and_time)
    time.sleep(2)


# Close Browser
def closeBrowser():
    driver.quit()


# RUNNER
ChromeBrowserCall(f"{base_url}/{endpoint}")
datePicker()
dateAndTimePicker()
closeBrowser()
