from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

cookie_url = "http://orteil.dashnet.org/experiments/cookie/"
service = Service("G:/chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get(cookie_url)

#finding the cookie
cookie = driver.find_element(By.ID, "cookie")

#initializing the timing variables
time_to_check = time.time() + 5    #5 seconds
five_minutes = time.time() + 5*60  #5 minutes

time_end = False

while time_end == False:
    #clicking on the cookie
    cookie.click()

    #checking the time
    if time.time() > time_to_check:
        can_buy = []
        #finding the upgrade elements
        upgrades = driver.find_elements(By.CSS_SELECTOR, "#store div")
        #buying the most expensive element we can afford
        for upgrade in reversed(upgrades):
            if upgrade.get_attribute("class") != "grayed":
                can_buy.append(upgrade)
        can_buy[0].click()
        #adding another 5 seconds
        time_to_check = time.time() + 5

    #if the time gets over five minutes, we end the loop
    if time.time() >= five_minutes:
        cookie_per_second = driver.find_element(By.ID, value="cps").text
        print(cookie_per_second)
        time_end = True

driver.quit()
