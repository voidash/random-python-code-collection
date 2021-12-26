import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


import pandas as pd

def read_csv():
    df= pd.read_csv("letter_final.csv")
    number_of_people = df.shape[0]
    for i in range(0,number_of_people):
        email = df['email'][i].strip()
        image = f'{i+1}.jpg'
        name = df['Name'][i]
        preamble = f'Dear Prof, \nOn behalf of the organizing committee of IAHR-Asia 2021, we would like to express our sincere gratitude to you for your contribution in the IAHR-Asia 2021 conference.\n\nIn the attachment, please find the report of the conference together with \'Letter of Appreciation\' from the conference Chair. \n\nThank you for your kind cooperation and support. \n\n---\nRegards,\nIAHR-Asia 2021\nTurbine Testing Lab,\nKathmandu University\nNepal'
        print(email)
        print(image)
        print(name)
        print(preamble)

    
def send_mail(emailto, fileToSend, preamble):
    emailfrom = "iahr.asia.2021@ku.edu.np"
    # emailto = "ashish.thapa477@gmail.com"
    # fileToSend = "1_.jpg"
    username = "iahr.asia.2021@ku.edu.np"
    password = "etst123"

    msg = MIMEMultipart()
    msg["From"] = emailfrom
    msg["To"] = emailto
    msg["Subject"] = "IAHR-ASIA 2021"
    msg.preamble = preamble

    ctype, encoding = mimetypes.guess_type(fileToSend)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)

    if maintype == "text":
        fp = open(fileToSend)
        # Note: we should handle calculating the charset
        attachment = MIMEText(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "image":
        fp = open(fileToSend, "rb")
        attachment = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "audio":
        fp = open(fileToSend, "rb")
        attachment = MIMEAudio(fp.read(), _subtype=subtype)
        fp.close()
    else:
        fp = open(fileToSend, "rb")
        attachment = MIMEBase(maintype, subtype)
        attachment.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
    pdf_attachment = MIMEText(open('IAHR-Asia-2021-report.pdf').read())
    msg.attach(attachment)
    msg.attach(pdf_attachment)


    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(username,password)
    server.sendmail(emailfrom, emailto, msg.as_string())
    server.quit()

read_csv()
