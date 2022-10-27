import os
from smtplib import SMTP

SMTP_HOST = os.environ["SMTP_HOST"]
SMTP_USER = os.environ["SMTP_USER"]
SMTP_PASSWORD = os.environ["SMTP_PASSWORD"]


def send_magic_link(magic_id, email):
    body = (
        "Hello! Here's your login link:\n\n" +
        "http://example.com/login/" + magic_id
    )
    send_email(email, "Login link", body)


def send_email(recipient, subject, body):
    message = (
        "From: " + SMTP_USER + "\n" +
        "To: " + recipient + "\n" +
        "Subject: " + subject + "\n\n" +
        body
    )
    with SMTP(host=SMTP_HOST, port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(user=SMTP_USER, password=SMTP_PASSWORD)
        smtp.sendmail(from_addr=SMTP_USER, to_addrs=recipient, msg=message)
