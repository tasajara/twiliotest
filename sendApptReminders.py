import json
from twilio.rest import Client
# replace <to_number> with appropriate phone number for testing
# replace <account_sid> and <auth_token> with appropriate values
# replace <from_number> with appropriate value

# get json data of appointments
appts_json = '''{
    "appointment1": {
            "name": "John Staley",
            "phone": "<to_number>",
            "dt": "Monday, August 26th at 2:30pm"
    },
    "appointment2": {
            "name": "Katherine Abernathy",
            "phone": "<to_number>",
            "dt": "Tuesday, August 27th at 8:30am"
    },
    "appointment3": {
            "name": "Franklin Longbottom",
            "phone": "<to_number>",
            "dt": "Wednesday, August 28th at 11:00am"
    }
}'''

# convert to data we can work with
appts = json.loads(appts_json)

# Account SID and Auth Token from twilio.com/console
account_sid = '<account_sid>'
auth_token = '<auth_token>'
from_number = '<from_number>'

# send appointment messages
client = Client(account_sid, auth_token)

for a in appts:
    print("From number:",from_number)
    print("Body:",appts[a]["dt"])
    print("To:",appts[a]["phone"])

    message = client.messages.create(
        from_= from_number,
        body= 'Hello, '+appts[a]["name"]+'! You have an upcoming appointment on '+ appts[a]["dt"]+" Please respond with CONFIRM or RESCHEDULE",
        to= appts[a]["phone"]
    )

    print("Message sent to",appts[a]["name"],"Message SID:",message.sid)
