import os
from flask import Flask, request
import twilio.twiml

if os.environ.get("VDM_ENVIRONMENT") == 'PROD':
    import settings.prod as settings
else:
    import settings

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/", methods=['GET', 'POST'])
def open_door():
    """Opens door if user requested it."""
    if request.values.get('Body') == settings.DOOR_OPEN_KEY:
        message = "Door Opened"
    else:
        message = "Unknown option selected"

    resp = twilio.twiml.Response()
    resp.sms(message)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
