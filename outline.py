import requests
import smtplib, ssl
import os
from email.mime.multipart import MIMEMultipart

websites = ["https://strona1.com", "https://strona2.com"]

def main():
    for website in websites:
        status = status_check(website)
        if status:
            send_email("Working")
        elif not status:
            send_email("Not working")


def status_check(address):
    #Takes website address as an argument and uses requests lib to check if status code is equal to 200
    r = requests.get(f"{address}")
    if r.status_code == "200":
        return True
    else:
        return False


def send_email(text, pages):
    #Sets up a safe connection to gmail (default, can be changed), imports password as an environmental variable and sends an email with arg message

    port = 465  # For SSL
    password = os.environ["PASSWORD_FOR_EMAIL_ACCOUNT"]

    # Create a secure SSL context
    context = ssl.create_default_context()
    msg = MIMEMultipart()
    msg['From']= #email nadawcy
    msg['To']= #email odbiorcy
    msg['Subject']= f"{page} is {text}"

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("my@gmail.com", password)
        server.sendmail(msg)


if __name__ == "__main__":
    main()
