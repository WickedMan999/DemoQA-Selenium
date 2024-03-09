from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# BASEURL
base_url = "https://demoqa.com"
endpoint = "select-menu"

# Customize Chrome Before It Opens
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")

# Opens Chrome Browser
driver = webdriver.Chrome(options=chrome_options)

# Explicit Wait Timer
wait = WebDriverWait(driver, 10)

# ActionChain Instance
actions = ActionChains(driver)


# Open URL
def ChromeBrowserCall(base_url):
    driver.get(base_url)
    driver.implicitly_wait(30)


def scrollDown():
    # Specify the number of times you want to scroll down
    scroll_count = 1

    # Specify the amount of scroll in pixels
    scroll_amount = 300

    # Scroll
    for i in range(scroll_count):
        driver.execute_script(f"window.scrollBy(0, {scroll_amount});")

    time.sleep(1)


def selectValue():
    # Here the dropdown menu is divided into 2 section, divied by | so to combine both of them and use it as a single element i used contains
    select_value = driver.find_element(
        By.XPATH, "//div[@id='withOptGroup']//div[contains(@class, ' css-tlfecz-indicatorContainer')]")
    select_value.click()

    # Select visible text named 'A root option' and click
    driver.find_element(By.XPATH, "//div[text()='A root option']").click()

    time.sleep(1)


def selectOne():
    # Here the dropdown menu is divided into 2 section, divied by | so to combine both of them and use it as a single element i used contains
    select_one_element = driver.find_element(
        By.XPATH, "//div[@id='selectOne']//div[contains(@class,' css-tlfecz-indicatorContainer')]")
    select_one_element.click()

    # Select visible text named 'Other' and click
    select_one = driver.find_element(By.XPATH, "//div[text()='Mrs.']")
    select_one.click()

    time.sleep(1)


def oldStyleSelectMenu():
    # Here the dropdown menu is divided into single section, so i don't have to use contains, i can just select it like normal element
    old_style_select = driver.find_element(
        By.XPATH, '//*[@id="oldSelectMenu"]')

    # Create Select Instance
    select = Select(old_style_select)

    # Select by visible text
    select.select_by_visible_text("Aqua")

    # Print the selected option
    print("Selected Color is: ", select.first_selected_option.text)

    time.sleep(1)


def multiSelectDropdown():
    # Here the dropdown menu is divided into 2 section, divied by | but here i used absolute xpath rather than custom writing one using contains
    element = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[7]/div/div/div/div[1]")))

    # Colors to select
    colors_to_select = ['Red', 'Blue', 'Green', 'Black']

    for color in colors_to_select:  # It will select all colors
        # Move to 'element' 'click' on element' & perform
        actions.move_to_element(element).click().perform()

        # Clear 'Move to element & click' action & perform new action i.e. 'send key:red' and rest of lists
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

    time.sleep(1)


def standardMultiSelect():
    # Here the dropdown menu is divided into single section, so i don't have to use contains, i can just select it like normal element
    multi_select = driver.find_element(By.CSS_SELECTOR, "#cars")

    # Create Select Object
    select = Select(multi_select)

    # Assuming 'select' is a Select object from Selenium and select all 4
    for i in range(4):
        select.select_by_index(i)

    time.sleep(1)


def closeBrowser():
    driver.quit()


# Runner
ChromeBrowserCall(f"{base_url}/{endpoint}")
scrollDown()
selectValue()
selectOne()
oldStyleSelectMenu()
multiSelectDropdown()
scrollDown()
standardMultiSelect()
closeBrowser()
