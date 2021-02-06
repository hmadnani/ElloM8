import os
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Say

#constants
 # the 10 digit number
FROM = '+12017302760' # our account
CALLED = ''+447444586906' # target accoount
account_sid = 'AC54a381894c4eb8c014a9dcfc939cbf16'
auth_token = '7d62fc795cb4c971c5bc38a2ae2e790b'

client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+447873211190',
                        from_='+12017302760'
                    )

print(call.sid)
