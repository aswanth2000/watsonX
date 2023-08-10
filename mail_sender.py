import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import ssl
import datetime

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
    today = datetime.date.today()
    f.write("IBM India\nSA3,Banglore \n"+str(today)+"\n\nDear "+json_data['name']+",\n\n    We are pleased to extend an offer of employment for the position of "+json_data['position']+" at IBM. We were highly impressed with your qualifications and experience , and we believe that you will be a valuable addition to our team.\n\nJob Title: "+json_data['position']+"\nLocation:Banglore\n\nYour employment with IBM will be on a Full-Time basis. Please note that your employment is contingent upon successfully passing a [Background Chec, etc.], which is standard procedure for all new employees.We are excited about the prospect of having you on our team and believe that your skills and experience will contribute to our continued success. We look forward to your positive response and to welcoming you to the IBM family. \n\nRegards, \nOnboarding Team")
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

