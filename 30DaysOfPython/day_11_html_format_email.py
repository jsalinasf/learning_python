import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


host = "smtp.gmail.com"
port = 587
username = "rethinktech18@gmail.com"
password = "COCOliso2012"
from_email = username
to_list = ["rethinktech18@gmail.com"]

the_msg = MIMEMultipart()

try:
    email_conn = smtplib.SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password)
    the_msg["Subject"] = "Project 01"
    the_msg["From"] = from_email
    # the_msg["To"] = to_list[0] #Remove comment and you will see this address in the "To" field of the recipient
    plain_text = "Message with Plain Text"
    html_text = """\
    <html>
    <head></head>
    <body>
        <p>Hi,<br>
            This Message is a <b>HTML</b> Message.<br>
            Made by Rethink Systems <a href="https://www.adistec.com">powered by Adistec</a>
        </p>
    </body>
    </html>    
    """
    part_1 = MIMEText(plain_text, "plain")
    part_2 = MIMEText(html_text, "html")
    the_msg.attach(part_1)
    the_msg.attach(part_2)
    email_conn.sendmail(from_email, to_list, the_msg.as_string())
    email_conn.quit()
except smtplib.SMTPException:
    print("Error sending message")
