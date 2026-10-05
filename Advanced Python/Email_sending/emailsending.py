# send email importsmtplib

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
# add sender or receiver details to send

sender_email='parmaramishc2520@gmail.com'
receiver_email='brijeshdeveloper36@gmail.com'
apppassword="curf ycrr quts yjlh"

# send email text
message=MIMEMultipart()
message["from"]=sender_email
message["to"]=receiver_email
message["subject"]="for sending email via python"
body="Respected Sir \n I am continuing my work right now and will make sure to practice and revise all the topics again \n Best Regars....\n Amish Parmar"

message.attach(MIMEText(body,"plain"))
#used exception handling to send email
file_path="logo.png"
try:
    # connect to send email with gmail server
    with open(file_path,"rb") as attachment:
        part=MIMEBase("application","octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Desposition",
            f"attachment; filename={file_path}"
        )
        message.attach(part)

    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender_email,apppassword)
    # send email via sendmail()
    server.sendmail(
        sender_email,
        receiver_email,
        message.as_string()
     )
except Exception as e:
    print("your email not send successfully",e)

finally:
    server.quit()
    
