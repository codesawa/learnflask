import os
import smtplib ,ssl
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from threading import Thread


def message_builder(message:str) -> MIMEMultipart:

    msg = MIMEMultipart()

    msg["From"] = message.from_email
    msg["To"] = message.to_email
    msg["Subject"] = message.subject

    # msg.attach(MIMEText(message.plain_msg, "plain"))
    msg.attach(MIMEText(message.html_msg, "html"))

    return msg


def smtp_setup(server:str, port:int) -> None:

    ssl_context = ssl.create_default_context()

    try:

        server = smtplib.SMTP(server, port)

        server.starttls(context=ssl_context)

        server.login("sehemumbalimbali@gmail.com","heslikuehtaqigpo") 


        return server

    except Exception:

        return
    
    

def send_mail(message:str, from_:str, to_:str) -> Thread:

    thr = Thread(target=send_mail_, args=[message, from_, to_])

    thr.start()

    return thr


def send_mail_(message:str, from_:str, to_:str) -> None:

    server = smtp_setup("smtp.gmail.com", 587)

    if server:

        message = message_builder(message)

        server.sendmail(from_, to_, message.as_string())

        server.quit()