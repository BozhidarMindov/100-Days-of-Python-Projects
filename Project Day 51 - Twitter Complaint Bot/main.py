from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

PROMISED_DOWN = 100
PROMISED_UP = 100
TWITTER_EMAIL = "bmindov.test@gmail.com"
TWITTER_PASSWORD = os.environ.get("PASSWORD")
TWITTER_USERNAME = os.environ.get("USERNAME")
service = Service("G:/chromedriver_win32/chromedriver")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=service)
        self.up = 0
        self.down = 0

    #gettign the internet speed
    def get_internet_speed(self):
        self.driver.maximize_window()
        self.driver.get("https://www.speedtest.net/")

        accept_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_button.click()
        time.sleep(3)

        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        time.sleep(50)

        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text


    #creating a tweet if my internet speed is lower that the pormised one
    def tweet_at_provider(self):
        if float(self.up) < PROMISED_UP or float(self.down) < PROMISED_DOWN:
            self.driver.get("https://twitter.com/login")
            time.sleep(3)

            email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
            email.send_keys(TWITTER_EMAIL)
            time.sleep(2)

            next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
            next_button.click()
            time.sleep(3)

            username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            username.send_keys(TWITTER_USERNAME)
            time.sleep(2)

            next_button_username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
            next_button_username.click()
            time.sleep(3)

            password = self.driver.find_element(By.CSS_SELECTOR, "input[type='password']")
            password.send_keys(TWITTER_PASSWORD)
            time.sleep(2)

            log_in_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
            log_in_button.click()
            time.sleep(2)

            tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
            tweet.click()
            time.sleep(2)

            tweet_text = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div")
            tweet_text.send_keys(f'Hey internet provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up ?')
            time.sleep(2)

            tweet_button = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]")
            tweet_button.click()
            time.sleep(3)


#creating the bot and calling its methods
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()