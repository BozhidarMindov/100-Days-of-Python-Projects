import smtplib
import datetime as dt
import random
import pandas

my_email1 = "bmindov.test@gmail.com"
password_gmail = "hidden"

letter_list = ["letter_templates/letter_1.txt",
               "letter_templates/letter_2.txt",
                "letter_templates/letter_3.txt"]

now = dt.datetime.now()
today = (now.month, now.day)

birthday_data = pandas.read_csv("birthdays.csv")
birthday_dict = {(birthday_data_row["month"], birthday_data_row["day"]): birthday_data_row for (index, birthday_data_row) in birthday_data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    with open(random.choice(letter_list)) as file:
        birthday_wish = file.read()
        birthday_wish = birthday_wish.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email1,
                         password=password_gmail)
        connection.sendmail(
            from_addr=my_email1,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{birthday_wish}"
        )
        connection.close()









