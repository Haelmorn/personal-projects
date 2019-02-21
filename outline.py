import requests
import smtplib, ssl
import os
from email.mime.multipart import MIMEMultipart
import datetime

websites = ["https://www.google.com/", "https://medium.freecodecamp.org/"]

def main():
    context = ssl.create_default_context()
    port = 587
    password = os.environ["PASSWORD_TO_EMAIL"]
    with smtplib.SMTP("smtp.gmail.com", port) as server:
        server.starttls(context=context)
        server.login("ciuchcia98@gmail.com", password)

        for website in websites:
            status = status_check(website)
            msg = compose_message(website, status)
            server.send_message(msg)

def status_check(address):
    # Takes website address as an argument and uses requests lib to check if status code is equal to 200
    try:
        r = requests.get(f"{address}")
        if r.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        write_log(e)

def compose_email(website, status):
    # builds message based on server response - status

    msg = MIMEMultipart()
    msg["From"] = "ciuchcia98@gmail.com"
    msg["To"] = "haelmorn@gmail.com"
    msg["Subject"] = f"{page} is {text}"

    return msg


def write_log(error_message):
    with open("logfile.txt", "a+") as log_file:
        now = datetime.datetime.now()
        log_file.write(str(now))
        log_file.write("\n")
        log_file.write(str(error_message))
        log_file.write("\n")


if __name__ == "__main__":
    main()

