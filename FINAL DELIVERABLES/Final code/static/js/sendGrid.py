import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='from@gmail.com',
    to_emails='to@gmail.com.com',
    subject='Sending demo mail with Twilio SendGrid',
    html_content='<strong> Sending  email with sendgrid using flask</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)

    