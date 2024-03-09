from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

# Variables
base_url = "https://demoqa.com"
endpoint = "automation-practice-form"
file_path = "D://Document//Mindrisers//11. Selenium//Final Codes//demoqa.com (final)//2. Forms//image.jpg"

# Customize Chrome Before It Opens
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")

# Opens Chrome Browser
driver = webdriver.Chrome(options=chrome_options)

# Wait Timer
wait = WebDriverWait(driver, 20)

# Actionchains Instance
actions = ActionChains(driver)


def scrollDown():
    # Calculate the height of the webpage
    page_height = driver.execute_script("return document.body.scrollHeight")

    # Specify the number of times you want to scroll down
    scroll_count = 1

    # Specify the amount of scroll in pixels
    scroll_amount = 400

    # Scroll
    for i in range(scroll_count):
        driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
    time.sleep(1)


# Open URL
def ChromeBrowserCall(base_url):
    driver.get(base_url)
    driver.implicitly_wait(30)


# Filling Form
def formFillUp(firstName, lastName, userEmail, contact, dob, address):
    # 1. Locate First Name element & Enter Firstname
    first_name = driver.find_element(
        By.XPATH, "//input[@id='firstName']")
    first_name.send_keys(firstName)
    print(first_name.text)

    # 2. Locate Last Name element & Enter Lastname
    last_name = driver.find_element(
        By.XPATH, "//input[@id='lastName']")
    last_name.send_keys(lastName)

    # Print Last name that was entered in text box
    typed_text = last_name.get_attribute('value')
    print(f"Last name is: {typed_text}")

    # 3. Locate Email element & Enter Email Address
    email_address = driver.find_element(
        By.XPATH, "//input[@id='userEmail']")
    email_address.send_keys(userEmail)

    # Print Email address that was entered in text box
    typed_text = email_address.get_attribute('value')
    print(f"Email address is: {typed_text}")

    # 4. Locate Gender element & Enter Select Gender | Just change on XPATH to select other gender
    gender = driver.find_element(
        By.XPATH, "//label[normalize-space()='Male']").click()

    # 5. Locate contact element & Enter contact detail
    contact_number = driver.find_element(
        By.XPATH, "//input[@id='userNumber']")
    contact_number.send_keys(contact)

    # Print Contact that was entered in text box
    typed_text = contact_number.get_attribute('value')
    print(f"Contact number is: {typed_text}")

    # 6. Locate DOB element and click it
    try:
        dateOfBirth = driver.find_element(
            By.XPATH, "//input[@id='dateOfBirthInput']")
        dateOfBirth.click()
        # Invoke CTRL + A, if i pressed backspace or remove current dob website will refresh
        dateOfBirth.send_keys(Keys.CONTROL + "a")
        # So without removing current dob i just enter new dob which wont refresh page
        dateOfBirth.send_keys(dob)
        # Once done i hit enter and it will format dob automatically
        dateOfBirth.send_keys(Keys.ENTER)

    except Exception as e:
        print("An error occurred:", e)

    # 7. Locate Subject element once it become clickable
    element = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="subjectsContainer"]')))

    # Colors to select
    subjects_to_select = ['Computer Science', 'Biology', 'History', 'English']

    # Select all Subjects using FOR loop
    for subject in subjects_to_select:
        # Move to 'element' 'click' on element' & perform
        actions.move_to_element(element).click().perform()
        time.sleep(1)

        # Clear 'Move to element & click' action & perform new action i.e. 'send key:Computer Science' and rest of list
        for i in subject:
            actions.send_keys(i).perform()
            actions.reset_actions()  # Reset the actions queue

        # Clear 'send key:Computer Science' action & perform new action i.e. 'send key:arrow down'
        actions.reset_actions()  # Reset the actions queue
        actions.send_keys(Keys.ARROW_DOWN).perform()

        # Clear 'send key:arrrow down' action & perform new action i.e. 'send key:return/enter'
        actions.reset_actions()  # Reset the actions queue
        actions.send_keys(Keys.ENTER).perform()

        # Print and confirm the selected color
        print(f"Multiple Color is: {subject}")

    time.sleep(1)

    # 8. Locate Hobbies element & select all hobbies using for loop
    hobbies = driver.find_elements(
        By.XPATH, "//div[@id='hobbiesWrapper']//div")

    # Click on each hobby element using FOR loop
    for hobby in hobbies:
        hobby.click()
        print(f"Hobbies are: {hobby.text}")

    # Scroll down
    scrollDown()

    # 9. Locate Upload Image element and upload the image once the upload button becomes clickable
    try:
        uploadPic = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@id='uploadPicture']")))
        uploadPic.send_keys(file_path)
        print("Image is uploaded")

    except:
        print("Failed to upload image")

    # 10. Locate Address element and enter the address
    current_address = driver.find_element(
        By.XPATH, "//textarea[@id='currentAddress']")
    current_address.send_keys(address)

    # Print Contact that was entered in text box
    typed_text = current_address.get_attribute('value')
    print(f"Contact number is: {typed_text}")

    # Click on Interaction and scroll so locate state and city can be visible
    interaction_menu_click = driver.find_element(
        By.XPATH, "(//div[contains(@class,'header-wrapper')])[5]")
    interaction_menu_click.click()
    time.sleep(2)

    # Scroll down
    scrollDown()

    # 11. Locate State element by combining XPATH
    select_state = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@id='state']//div[contains(@class,' css-tlfecz-indicatorContainer')]")))
    select_state.click()

    # Select visible text named 'NCR' and click
    state = driver.find_element(By.XPATH, "//div[text()='NCR']")
    state.click()

    # 12. Locate city element by combining XPATH
    city = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@id='city']//div[contains(@class, ' css-tlfecz-indicatorContainer')]")))
    city.click()

    # Select visible text named 'Noida' and click
    state = driver.find_element(By.XPATH, "//div[text()='Noida']")
    driver.execute_script("arguments[0].click();", state)

    # 13. Locate Sumbit button element once button become visible
    sumbit_button = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="submit"]')))

    # Press submit button using JavaScript
    driver.execute_script("arguments[0].click();", sumbit_button)

    time.sleep(2)


# Close Browser
def closeBrowser():
    driver.quit()


# RUNNER
ChromeBrowserCall(f"{base_url}/{endpoint}")
scrollDown()
formFillUp('Wicked', 'Man', 'wickedman@gmail.com',
           '9849984998', '11-Feb-1999', 'Kirtipur')
closeBrowser()
