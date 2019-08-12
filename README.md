#Twilio test for interview by Matthew Stevenson
This code is skeleton for client to work from showing how the SMS sending
and processing would work.

* sendApptReminders.py takes JSON data of appointments that need to be confirmed
and sends out the text messages.

* sms.py is the receiving server that processes the SMS received and looks for either
CONFIRM or RESCHEDULE and sends a response message back accordingly.
  - A Webhook pointing to the receiving server is required to route the patient
  SMS messages to this server.
