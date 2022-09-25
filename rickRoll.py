from twilio.rest import Client

#credentials
account_sid = "AC61b4d94b41f3c34d18b86724ec97a893"
auth_token = "1eecec2846bb4b61dd797731bb695cfe"
client = Client(account_sid, auth_token)
#Enter your own number in to=""
call = client.calls.create(to="+91987654321" , from_="+19289637327", url="http://twimlets.com/AC751ad5243c75ae17aaf9b1db18decd96/rickroll",
	IfMachine="Hangup")

print (call.sid)