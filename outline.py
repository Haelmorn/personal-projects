import requests
import smtplib, ssl
import os
from email.mime.multipart import MIMEMultipart
import datetime

websites = ["https://www.google.com/", "https://medium.freecodecamp.org/"]


def main():
    for website in websites:
        status = status_check(website)
        if status:
            send_email("working", website)
        elif not status:
            send_email("not working", website)


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


def send_email(text, page):
    # Sets up a safe connection to gmail (default, can be changed), imports password as an environmental variable and sends an email with arg message

    port = 587
    password = os.environ["PASSWORD_TO_EMAIL"]

    # Create a secure SSL context
    context = ssl.create_default_context()
    msg = MIMEMultipart()
    msg["From"] = "ciuchcia98@gmail.com"
    msg["To"] = "haelmorn@gmail.com"
    msg["Subject"] = f"{page} is {text}"

    with smtplib.SMTP("smtp.gmail.com", port) as server:
        server.starttls(context=context)
        server.login("ciuchcia98@gmail.com", password)
        server.send_message(msg)


def write_log(error_message):
    with open("logfile.txt", "a+") as log_file:
        now = datetime.datetime.now()
        log_file.write(str(now))
        log_file.write("\n")
        log_file.write(str(error_message))
        log_file.write("\n")


if __name__ == "__main__":
    main()
