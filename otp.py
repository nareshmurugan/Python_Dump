import twilio
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import random # generate random number
otp = random.randint(1000,9999)
print("Your OTP is - ",otp)
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACbe79510c8a2a3c52a65fdb96910243eb'
auth_token = '5543c10506701dedfb434c8dfc0ffce6'
client = Client(account_sid, auth_token)

message = client.messages.create(
         body='Hello Mr. Mayur Your Secure Device OTP is - ' + str(otp) + 'now your mobile is hacked!\n Byby...',
         from_="+919486691874",
         to="+919489228333"
     )

print(message.sid)
