import smtplib

sender = "<email>"
reciver =  "<recEmail>"
password =  "password"
subject =  "test"
body =  "lorem ipsum72"

# ?header
message = f"""From: {sender}
To: {reciver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
try:
    server.login(sender, password)
    print("logged in...")
    server.sendmail(sender, reciver, message)
    print("email has been send")
except smtplib.SMTPAuthenticationError:
    print("unable to sign in")