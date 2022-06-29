import requests
from bs4 import BeautifulSoup
import os
import smtplib
import lxml.html

s22_ultra_url = "https://www.amazon.com/SAMSUNG-Smartphone-Unlocked-Brightest-Processor/dp/B09MVZ93YN/ref=sr_1_1_sspa?crid=70O11Y72SKAM&keywords=samsung+galaxy+s22&qid=1656487491&sprefix=samsung+gala%2Caps%2C162&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFIQzBMRlg0Ukw1Q1gmZW5jcnlwdGVkSWQ9QTA0OTY3NDUxQ1lGQkg1N01VSkJEJmVuY3J5cHRlZEFkSWQ9QTA5NzQ2MzIzUU5QTk9LMThRN0smd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"
my_email1 = "bmindov.test@gmail.com"
password_gmail = os.environ.get("PASSWORD")
INSTANT_BUY_PRICE = 1100

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9,bg-BG;q=0.8,bg;q=0.7,en-US;q=0.6"
}

response = requests.get(url=s22_ultra_url, headers=headers)
#scraping for data (product title/product price)
soup = BeautifulSoup(response.text, "lxml")

product = soup.find(name="span", class_="a-offscreen").get_text()
only_price = product.split("$")[1]
float_as_price = float(only_price.replace(",", ""))

title = soup.find(id="productTitle").get_text().strip()

#sending us an email if the price of the product is below our desired max prioce
if float_as_price < INSTANT_BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email1,
                         password=password_gmail)
        connection.sendmail(
            from_addr=my_email1,
            to_addrs=my_email1,
            msg= f"Subject: Amazon Price Alert! \n\n{title} is now ${only_price}.\n{s22_ultra_url}"
        )
        connection.close()
