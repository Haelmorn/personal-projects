# -*- coding: UTF-8 -*-
import requests
import smtplib, ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime


#READ ME
#All placeholder values are preceded with a '#'.  Those need to be changed for the script to work
websites = ["#website1", "#website2"]


def main():
    try:
        context = ssl.create_default_context()
        port = 587
        password = os.environ["PASSWORD_TO_EMAIL"]
        with smtplib.SMTP("smtp.gmail.com", port) as server:
            server.starttls(context=context)
            server.login("#sender_email", password)

            for website in websites:
                status = status_check(website)
                msg = compose_email(website, status)
                server.send_message(msg)
    except Exception as e:
        write_log(e)


def status_check(address):
    """Takes website address as an argument and uses requests
    lib to check if status code is equal to 200"""
    try:
        r = requests.get(f"{address}")
        if r.status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False


def compose_email(website, status, error_message=''):
    # builds message based on server response - status
    msg = MIMEMultipart()
    msg["From"] = "#sender_email"
    msg["To"] = "#recipient_email"
    if status == True:
        msg["Subject"] = u"\u2713 STATUS OK: {}".format(website)
        write_log(f"STATUS OK: {website}")
    else:
        try:
            code = requests.get(f"{website}").status_code
        except Exception as e:
            code = e
        msg["Subject"] = u"\u274C ERROR {}: {}".format(code,website)
        write_log(f"ERROR {code}: {website}")

    return msg


def write_log(log_message):
    with open("logfile.txt", "a+") as log_file:
        now = datetime.datetime.now()
        log_file.write(str(now))
        log_file.write(" - ")
        log_file.write(str(log_message))
        log_file.write("\n")


if __name__ == "__main__":
    main()

