import os

from flask import Flask, request
import phone
import settings
import twilio.twiml


app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/open_door", methods=['GET', 'POST'])
def open_door():
    """ Opens door if user requested it. """
    if request.values.get('Body') == settings.DOOR_OPEN_KEY:
        message = "Door Opened"
    else:
        message = "Unknown option selected"

    resp = twilio.twiml.Response()
    resp.sms(message)

    return str(resp)


@app.route("/buzzer_pressed", methods=['GET', 'POST'])
def buzzer_pressed():
    """ Called when the buzzer is pressed """
    response = phone.notify_buzzer_pressed()
    return str(response)


def start_webserver():
    """ launches the flask webserver """
    app.run(debug=True)
