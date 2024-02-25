import smtplib      #El correo funciona por SMTP
import os
from email.mime.text import MIMEText

print("send Email")
client= smtplib.SMTP(host='localhost',port=1025)
sender= 'tesan.deale22@zaragoza.salesianos.edu'
dest='ventura.tocar22@zaragoza.salesianos.edu'
message=""

with open("texto_desencriptado.txt", "r") as file:
    text = file.read()
    message = MIMEText(text, 'plain')

message_template='From:%s\r\nTo:%s\r\n\r\n%s'
client.set_debuglevel(1)
client.sendmail(sender,dest,message_template%(sender,dest,message))
client.quit()
print("Email end")


























"""import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración del servidor SMTP
smtp_server = 'smtp.tu_servidor_smtp.com'
smtp_port = 587  # Puerto SMTP (puede variar según la configuración del servidor)
smtp_username = 'tu_correo@gmail.com'  # Tu dirección de correo electrónico
smtp_password = 'tu_contraseña'  # Tu contraseña de correo electrónico

# Direcciones de correo electrónico
sender_email = 'tu_correo@gmail.com'
receiver_email = 'correo_destinatario@example.com'

# Crear el mensaje
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Asunto del correo'

# Cuerpo del correo
body = 'Hola, este es un correo de prueba enviado desde Python.'
message.attach(MIMEText(body, 'plain'))

# Iniciar sesión en el servidor SMTP
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Habilitar el cifrado TLS
server.login(smtp_username, smtp_password)

# Enviar correo electrónico
server.sendmail(sender_email, receiver_email, message.as_string())

# Cerrar sesión en el servidor SMTP
server.quit()

print("Correo enviado exitosamente")"""
