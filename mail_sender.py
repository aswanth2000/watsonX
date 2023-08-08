import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
def send_mail(json_data):
    sender = "watson_dragons@noreply.com"   
    msg = MIMEMultipart()
    msg['Subject'] = json_data['mail_subject']
    msg['From'] = sender
    recipients=[json_data['mail_to']] 
    msg['To'] = ", ".join(recipients)
    msg.preamble = 'Multipart massage.\n'
    message = json_data['mail_body']
    msg.attach(MIMEText(message))
    filename ="./sample.txt"
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(filename, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % filename)
    msg.attach(part)
    print("Inside Mail Sender")
    server = smtplib.SMTP('ap.relay.ibm.com')
    for i in recipients:
        server.sendmail(msg['From'], i, msg.as_string())
    server.close()
    print("Mail sent")
    return "Mail Successfully went"