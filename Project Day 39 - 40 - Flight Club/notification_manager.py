import smtplib
import os

my_email1 = "bmindov.test@gmail.com"
password_gmail = os.environ.get("PASSWORD")

class NotificationManager:
    def send_notification(self, msg, emails):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email1,
                             password=password_gmail)
            for email in emails:
                connection.sendmail(
                    from_addr=my_email1,
                    to_addrs=email,
                    msg=msg
                )
            connection.close()