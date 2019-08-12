from flask import Flask, request, redirect
from twilio.twiml.messaging_response import Message, MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])

def sms_reply():
    # Get message sent
    message_body = request.form['Body'].upper()

    if message_body.find('CONFIRM') >= 0:
        msg_reply = "Thanks for the confirmation!"

    elif message_body.find('RESCHEDULE') >= 0:
        msg_reply = "It appears you need to cancel or change your appointment, we will contact you."

    else:
        msg_reply = f"Unknown response: '{message_body}' - Please respond with CONFIRM or RESCHEDULE."


    # TwiML response
    resp = MessagingResponse()
    resp.message(msg_reply)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
