import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path

email    = 'fotocrypto@gmail.com'
password = 'Fotocrypto secure1554'

def send_verfication(ucode, account):
    """Esta función recibe como primer párametro el código de verficación, en el segundo la dirección de correo del usuario"""
    vcode   = ucode
    send_to = account
    
    css          = 'body { font-size:18px;font-family:sans-serif;width:80%;margin:10px auto;box-sizing:border-box}.code{text-align:center;padding:20px;background-color:#ff6b6b;width:100px;margin:30px auto}.code span{font-weight:700;color:white;font-size:20px}'
    subject      = 'Verificación de Cuenta'
    messageHTML  = f"<!DOCTYPE html><html><head><meta charset='UTF-8'><title>Verficación de Código</title><style>{css}</style></head><body><div class='main'><div class='msg'><p>En este correo te proporcionaremos el código de verficación para poder crear tu cuenta, por favor no respondas a este email ni tampoco se lo muestres a nadie.</p> <strong>Si no solicitaste crear una cuenta, ignora este correo.</strong></div><p class='code'> <span>{vcode}</span></p></div></body></html>"
    messagePlain = f'En este correo te proporcionaremos el código de verficación para poder crear tu cuenta, por favor no respondas a este email ni tampoco se lo muestres a nadie.\nSi no solicitaste crear una cuenta, ignora este correo.\n{vcode}'

    msg = MIMEMultipart('alternative')
    msg['From']    = email
    msg['To']      = send_to
    msg['Subject'] = subject

    msg.attach(MIMEText(messagePlain, 'plain'))
    msg.attach(MIMEText(messageHTML, 'html'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to, text)
    server.quit()
