import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os


API_KEY = os.environ.get("OWM_API_KEY")
url = "https://api.openweathermap.org/data/2.5/weather"
TRIAL_PHONE_NUMBER = "+12602170246"
account_sid = "ACeffa472c7d93d4e13b2179c0c25ca0b3"
auth_token = os.environ.get("AUTH_TOKEN")
one_call_url = "https://api.openweathermap.org/data/2.5/onecall/timemachine"

parameters = {
    "lat": 42.43278,
    "lon": 25.64194,
    "dt": 1655732101,
    "exclude":"current,minutely,daily",
    "appid": API_KEY
}

response = requests.get(one_call_url, params=parameters)
response.raise_for_status()

will_rain = False

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
    client = Client(account_sid,auth_token, http_client= proxy_client)
    message = client.messages \
                    .create(
                        body="It is going to rain! Bring an umbrella!",
                        from_=TRIAL_PHONE_NUMBER,
                        to="hidden"
                    )

    print(message.status)

