from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9,bg-BG;q=0.8,bg;q=0.7,en-US;q=0.6"
}

forms_url = os.environ.get("FORMS_URL")
zillow_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-123.51273573828125%2C%22east%22%3A-121.35392226171875%2C%22south%22%3A37.48708129572077%2C%22north%22%3A38.06238242908446%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A9%7D"

response = requests.get(url=zillow_url, headers=headers)

#accessing the Zillow website and extarcting data for adresses, links and prices
soup = BeautifulSoup(response.text, "html.parser")
link_elements = soup.select(".list-card-top a")

links = []
for link in link_elements:
    href = link["href"]
    if "http" not in href:
        links.append(f"https://www.zillow.com{href}")
    else:
        links.append(href)

address_elements = soup.select(".list-card-info address")
addresses = []
for address in address_elements:
    addresses.append(address.get_text().split(" | ")[-1])

price_elements = soup.find_all("div", {"class": "list-card-price"})
prices = []
for price in price_elements:
    if "$" in price.text:
        if "/mo" in price.get_text().split("+")[0]:
            prices.append(price.get_text().split("+")[0].replace("/mo", ""))
        else:
            prices.append(price.get_text().split("+")[0])

service = Service("G:/chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=service)

#wiritng our accessed data to a google form, which is then saved onto a google sheet
for i in range(len(links)):
    driver.get(forms_url)
    time.sleep(3)

    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(addresses[i])
    time.sleep(2)

    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(prices[i])
    time.sleep(2)

    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(links[i])
    time.sleep(2)

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
    submit_button.click()

driver.quit()
