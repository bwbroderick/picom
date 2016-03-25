from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
_ACCOUNT_SID = "AC07829106f269b0a4d58e0dfaf9fefed6"
_AUTH_TOKEN = "130f05e8cea44aa47076df8835affed4"


def send_sms(to, from_, body):
    client = TwilioRestClient(_ACCOUNT_SID, _AUTH_TOKEN)
    message = client.messages.create(to=to, from_=from_,
                                     body=body)
    return message


def notify_buzzer_pressed():
    send_sms(to="9042546759", from_="9044970273",
             body="The front door buzzer has been pressed!")
