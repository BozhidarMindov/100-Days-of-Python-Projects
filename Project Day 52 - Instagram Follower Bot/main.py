from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

SIMILAR_ACCOUNT = os.environ.get("ACCOUNT")
USERNAME = os.environ.get("NAME")
PASSWORD = os.environ.get("PASSWORD")
LOGIN_URL = "https://www.instagram.com/accounts/login/"


class InstaFollower:
    #Initialization
    def __init__(self, service):
        self.driver = webdriver.Chrome(service=service)

    #login method
    def login(self):
        self.driver.get(LOGIN_URL)
        self.driver.maximize_window()

        allow_cookies = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[2]')
        allow_cookies.click()
        time.sleep(1)

        username_entry = self.driver.find_element(By.NAME, "username")
        username_entry.send_keys(USERNAME)
        time.sleep(1)

        password_entry = self.driver.find_element(By.NAME, "password")
        password_entry.send_keys(PASSWORD)
        time.sleep(1)

        log_in_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        log_in_button.click()
        time.sleep(5)

    #locating the followers button and scroling on it
    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(3)

        followers = self.driver.find_element(By.PARTIAL_LINK_TEXT, "followers")
        followers.click()
        time.sleep(10)

        modal = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[2]")

        for i in range(10):
            try:
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', modal)
                time.sleep(5)
                print("scrolled")
            except NoSuchElementException:
                pass

    #following all the people
    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR,"li button")

        for i in follow_buttons:
            try:
                i.click()
                time.sleep(5)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

            print("All people followed")


bot = InstaFollower(Service("G:/chromedriver_win32/chromedriver"))
bot.login()
bot.find_followers()
bot.follow()