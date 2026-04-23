import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv


load_dotenv()

EMAIL = os.getenv("EMAIL")
EMAIL_PASS = os.getenv("EMAIL_PASS")


def send_email(receiver, subject, body):

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = receiver

    server = smtplib.SMTP("smtp.gmail.com", 587)

    try:
        server.starttls()
        server.login(EMAIL, EMAIL_PASS)
        server.sendmail(EMAIL, receiver, msg.as_string())

    finally:
        server.quit()
