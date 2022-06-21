import requests
import smtplib
import os

my_email1 = "bmindov.test@gmail.com"
password_gmail = os.environ.get("PASSWORD")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_STOCK = os.environ.get("STOCK_API_KEY")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY_NEWS = os.environ.get("NEWS_API_KEY")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": API_KEY_STOCK
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_close_price = float(data_list[0]["4. close"])
day_bef_yesterday_close_price = float(data_list[1]["4. close"])

diff = (yesterday_close_price - day_bef_yesterday_close_price)

up_down = None
if diff < 0:
    up_down ="⬇"
elif diff > 0:
    up_down = "⬆"


diff_percent = round((diff/yesterday_close_price) * 100)

#if the difference in percentage rise or fall is greater than 1, an email will be sent to us
if abs(diff_percent) > 1:
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": API_KEY_NEWS
    }

    news_response = requests.get(NEWS_ENDPOINT, news_parameters)
    articles = news_response.json()["articles"]

    first_three_articles = articles[:3]
    print(first_three_articles)


    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in first_three_articles]


    for article in formatted_articles:
        msg = f"Subject: Tesla Stock News!\n\n{article}".encode('utf-8', errors="ignore")

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email1,
                             password=password_gmail)
            connection.sendmail(
                from_addr=my_email1,
                to_addrs=my_email1,
                msg=msg
            )
            connection.close()


