import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "tt.ethernet.2021@gmail.com"
receiver_email = "tt.ethernet.2021+receiver@gmail.com"
password = "CisloDzialowy"

message = MIMEMultipart("alternative")
message["Subject"] = "Html/multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version
text = """\
Hi,
How are you?
Microeletronics in Industry and Medicine is the best!
http://www.mtm.agh.edu.pl/"""
html = """\
<html>
  <body>
    <p>Hi,<br>
      <b>How are you?</b><br>
      <a href="http://www.mtm.agh.edu.pl/">Microeletronics in Industry and Medicine</a>
      is the best!
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
