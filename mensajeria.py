#libreria para enviar correos
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from os import environ

def enviar_email(destinatario,asunto,cuerpo):
    
    email_emisor = environ.get('CORREO_EMISOR')
    password_emisor = environ.get('PASSWORD_EMISOR')

    #AHORA CREAMOS EL CUERPO

    cuerpo_del_correo= MIMEText(cuerpo,'plain')

    correo = MIMEMultipart()

    correo['Subject'] = asunto
    correo['To'] = destinatario
    # ahora adjuntamos al corre el texto
    correo.attach(cuerpo_del_correo)
    
    # Procedemos con el envio
    # outlook > outlook.office365.com | 587
    # hotmail > smtp.live.com         | 587
    # gmail >   smtp.gmail.com        | 587
    # icloud >  smtp.mail.me.com      | 587
    # yahoo >   smtp.mail.yahoo.com   | 465
    manejador_correo = SMTP('smtp.gmail.com', 587)
    #print(email_emisor,password_emisor)
    manejador_correo.starttls()
    manejador_correo.login(email_emisor,password_emisor)

    #enviar correo
    manejador_correo.sendmail(from_addr=email_emisor,
                              to_addrs=destinatario,
                              msg=correo.as_string())
    manejador_correo.quit()

    print('Correo enviado existosamente')


