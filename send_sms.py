from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC07829106f269b0a4d58e0dfaf9fefed6"
auth_token = "130f05e8cea44aa47076df8835affed4"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="9042546759", from_="9044970273",
                                 body="Hello there!")
