# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['ACa57f10c435bb447a5e0098907718c894']
auth_token = os.environ['9eb11f818374a53f178b35cd0fc5978f']
client = Client(account_sid, auth_token)
num=233566545754 # phone number
too="f+91{num}"
message = client.messages.create(
                     body="Join Earth's mightiest heroesdsgdfd. Like Kevin Bacon.",
                     from_='+15017122661',
                     to=too
                 )

print(message.sid)
