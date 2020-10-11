from twilio.rest import Client

sid = "AC5e19b7599360cb58f403c3b30cd8b57b"

token = "cc17e3df6d130c7711fc752f479704b0"

client = Client(sid, token)

msg = client.messages.create(
    to="+886933411413",
    from_="+14243221168",
    body="Test.")

print(msg.sid)