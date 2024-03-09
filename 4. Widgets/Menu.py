from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


# BASEURL
base_url = "https://demoqa.com"
endpoint = "menu"

# Customize Chrome Before It Opens
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")

# Opens Chrome Browser
driver = webdriver.Chrome(options=chrome_options)

# Explicit Wait Timer
wait = WebDriverWait(driver, 30)

# Actionchain instance
action = ActionChains(driver)


# Open URL
def ChromeBrowserCall(base_url):
    driver.get(base_url)


def mainMenu2():
    # Locating Element Using Explicit Wait
    main_item_2 = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//a[normalize-space()='Main Item 2']")))

    # Hover to 'main menu 2' using actionchains
    action.move_to_element(main_item_2).perform()
    time.sleep(1)

    # Under 'main menu 2' locate 'Sub List'
    sub_list = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/a')))

    # Hover to 'Sub List' using actionchains
    action.move_to_element(sub_list).perform()
    time.sleep(1)

    # Hover on 'sub list 2' under 'Sub List'
    sub_list_2 = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/ul/li[2]/a')))

    # Hover to 'sub list 2' using actionchains
    action.move_to_element(sub_list_2).perform()
    time.sleep(2)


def closeBrowser():
    driver.quit()


# RUNNER
ChromeBrowserCall(f"{base_url}/{endpoint}")
mainMenu2()
closeBrowser()
