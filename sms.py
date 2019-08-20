# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC8a1b8bfdc60cbd0663511b0e60280b91'
auth_token = 'f91892eebfc048b35735dc03aceaebb0'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+56937100595',
         to='+56979892505'
     )

print(message.sid)
