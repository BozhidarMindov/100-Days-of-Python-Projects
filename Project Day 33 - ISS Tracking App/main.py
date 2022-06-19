import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 42.423920
MY_LONG = 25.624901

my_email1 = "bmindov.test@gmail.com"
password_gmail = "hidden"

#a function that checks if The ISS is overhead
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    else:
        return False

#a function that checks if it is night time
def is_nighttime():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False

#infinite loop that executes every 60 seconds
#if the ISS is overhead and it is night time, an email will be sent to us
while True:
    time.sleep(60)
    if is_iss_overhead() == True and is_nighttime() == True:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email1,
                            password=password_gmail)
            connection.sendmail(
                from_addr=my_email1,
                to_addrs=my_email1,
                msg="Subject: Look Up \n\nThe ISS is overhead."
            )
            connection.close()




