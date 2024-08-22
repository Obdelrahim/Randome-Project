import random
import ssl
import smtplib
from email.message import EmailMessage

names = ['Name']
print(names)

random.shuffle(names)
print("Shuffled order:", names)

emailname = 'placeholder@gmail.com'
emailpass = ''
emailrecip=['placeholders@gmail.com']

# Email construction
sub = 'Monday League Draft Positions 2024'
body = 'Below is the 2024 draft order for the Monday Fantasy Football League:\n\n'
for i, name in enumerate(names, 1):
    body += f'{i}. {name}\n'

# Create email message
em = EmailMessage()
em['From'] = emailname
em['To'] = emailrecip
em['Subject'] = sub
em.set_content(body)
context = ssl.create_default_context()

# send email
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(emailname, emailpass)
        smtp.send_message(em)
    print("Email Sent.")
except smtplib.SMTPAuthenticationError:
    print("Authentication Failed.")
except Exception as e:
    print(f"Error: {e}")