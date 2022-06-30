#CODE DOESN'T WORK
#even when trying solutions online, the code is not running properly and the correct elements are not being found




from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebElement

email = "mindov0249@gmail.com"
password = "hidden"
phone_number = "hidden"


job_url = "https://www.linkedin.com/jobs/search/?currentJobId=3006939588&f_AL=true&geoId=105333783&keywords=remote%20internship&location=Bulgaria"
service = Service("G:/chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get(job_url)
driver.maximize_window()

sign_in = driver.find_element(By.LINK_TEXT,"Sign in")
sign_in.click()

email_entry = driver.find_element(By.ID, "username")
email_entry.send_keys(email)

password_entry = driver.find_element(By.ID, "password")
password_entry.send_keys(password)


submit_button = driver.find_element(By.CSS_SELECTOR,".login__form_action_container button")
submit_button.submit()

listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-list")
print(listings)

for listing in listings:
    listing.click()

    try:
        easy_apply_btn: WebElement = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
        easy_apply_btn.click()

        phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(phone_number)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CSS_SELECTOR,"artdeco-modal__dismiss")
            close_button.click()

            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("Skipped.")
        continue
driver.quit()


