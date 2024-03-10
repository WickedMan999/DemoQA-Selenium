from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import pyautogui  # For clicking save button on explorer popup

# Variable
baseURL = "https://demoqa.com"
endpoint = "upload-download"


# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")


# Create Chrome WebDriver instance
driver = webdriver.Chrome(options=chrome_options)


# Open URL
def ChromeBrowserCall(baseURL):
    driver.get(baseURL)
    driver.implicitly_wait(30)


# Wait Timer
wait = WebDriverWait(driver, 20)


def upload():
    # File to upload
    upload_file = "D:\\upload.jpg"

    # Click on the 'Upload File' button to open file dialog box
    upload = driver.find_element(By.CSS_SELECTOR, "#uploadFile")

    # Transfer upload file
    upload.send_keys(upload_file)
    print("Upload successful")
    time.sleep(3)


def download():
    download_file = driver.find_element(
        By.CSS_SELECTOR, "#downloadButton")
    download_file.click()

    # Wait for the "Save As" dialog to load
    time.sleep(2)

    # Press "Enter" to save the file
    pyautogui.press('enter')
    time.sleep(2)

    print("Download successful")


# RUNNER
ChromeBrowserCall(f"{baseURL}/{endpoint}")
# upload()
download()
