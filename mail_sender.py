import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import ssl
def send_mail(json_data):
    sender = "watsonx035@gmail.com" 
    password = "akvfwflrjyehigfk"  
    msg = MIMEMultipart()
    msg['Subject'] = json_data['mail_subject']
    msg['From'] = sender
    recipients=[json_data['mail_to']] 
    msg['To'] = ", ".join(recipients)
    msg.preamble = 'Multipart massage.\n'
    message = json_data['mail_body']
    f = open(json_data['name']+"-offerLetter.txt", "w")
    f.write("Hi"+json_data['name']+",\nWelcome to IBM. \nRegards, \nOnboarding Team")
    f.close()
    msg.attach(MIMEText(message))
    filename =json_data['name']+"-offerLetter.txt"
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(filename, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % filename)
    msg.attach(part)
    print("Inside Mail Sender")
    context = ssl.create_default_context()
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.starttls(context = context)
    server.login(sender, password)
    for i in recipients:
        server.sendmail(msg['From'], i, msg.as_string())
    server.close()
    print("Mail sent")
    return "Mail Successfully went"
