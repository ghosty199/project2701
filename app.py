# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/login')
def index():
    return render_template('home.html')


# Define route and Verify_otp() function below

def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']
    if username == 'verify' and password == '12345':
        account_sid="AC0ef4849877036239de878d1fef00c20c"
        auth_token="47628692858e72a3cd6741222b2519d1"
        client=Client(account_sid, auth_token)
        

        verification = client.verify \
            .services('Enter service sid from twilio') \
            .verifications \
            .create(to=enter mobile number variable here, channel='sms')










if __name__ == "__main__":
    app.run()

