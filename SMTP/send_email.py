import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "tt.ethernet.2021@gmail.com"
receiver_email = "tt.ethernet.2021+receiver@gmail.com"
password = "CisloDzialowy"
message = """\
Subject: Echo

This message was sent by me."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
