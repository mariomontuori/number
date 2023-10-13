import email, smtplib, ssl
import time
from flask import Flask, request, jsonify
from providers import PROVIDERS

from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

def send_sms_via_email(
    number: str,
    message: str,
    provider: str,
    sender_credentials: tuple,
    subject: str = "",
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 465,
):
    sender_email, email_password = sender_credentials
    receiver_email = f'{number}@{PROVIDERS.get(provider).get("sms")}'

    email_message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

    with smtplib.SMTP_SSL(
        smtp_server, smtp_port, context=ssl.create_default_context()
    ) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, email_message)

#@app.route("/main/<string:number>/<string:email>/<string:password>")
def main():
    #number = 'number'
    #email = 'email'
    #password = 'password'

    #message = "Yo What's Up!"
    #provider = "Verizon"

    #sender_credentials = (email, password)

    #time.sleep(10)

    #send_sms_via_email(number, message, provider, sender_credentials)

    return "sent"


if __name__ == "__main__":
    app.run(debug=True)
    #main()
