import paramiko
from scp import SCPClient
import smtplib
import os
from email.mime.text import MIMEText
from ftplib import FTP
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from http.server import BaseHTTPRequestHandler, HTTPServer

class Principal():
    def __init__(self):
        self.directorio_actual = ''

    def pasos(self):
        self.iniciarServidorHTTP()

    def conexionSSH(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(hostname='192.168.1.123', port=2222, username='tresdos', password='tresdos')
            print("-Conectado por SSH...")

            self.MostrarDirectorioActualSSH(ssh)
            self.CambiarDirectorioSSH(ssh, '/home')
            self.MostrarDirectorioActualSSH(ssh)
            self.MostrarDirectoriosSSH(ssh)

            print('Descargando ...')
            scp = SCPClient(ssh.get_transport())
            scp.get('/home/private.pem')  
            scp.get('/home/encrypted_data.bin')
            print('Descarga completada')

            self.descifrar()
            self.enviarCorreo()
            self.enviarFTP()

        # Posibles excepciones
        except paramiko.AuthenticationException:
            print("Error de autenticación. Asegúrate de que las credenciales sean correctas.")
        except paramiko.SSHException as e:
            print("Error de conexión SSH:", e)
        finally:
            ssh.close()

    def descifrar(self):
        print("\n-descifrando ..-")
        with open("private.pem", "rb") as key_file:
            private_key_data = key_file.read()
        
        private_key = RSA.import_key(private_key_data)

        with open("encrypted_data.bin", "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()

        # Descifrado utilizando la clave privada
        cipher_rsa = PKCS1_OAEP.new(private_key)
        decrypted_data = cipher_rsa.decrypt(encrypted_data)

        # Escribir datos descifrados en un nuevo archivo
        with open("archivo_descifrado.txt", "wb") as decrypted_file:
            decrypted_file.write(decrypted_data)

        print("Archivo descifrado con éxito.")
        print("Valor del archivo descifrado:", decrypted_data.decode())  

    def enviarCorreo(self):
        print("\n-enviando Correo ...")
        client= smtplib.SMTP(host='192.168.1.123', port=1023)
        sender= 'tesan.deale22@zaragoza.salesianos.edu'
        dest='gorka.sanz@zaragoza.salesuanos.edu'
        message=""

        with open("archivo_descifrado.txt", "r") as file:
            text = file.read()
            message = MIMEText(text, 'plain')

        message_template='From:%s\r\nTo:%s\r\n\r\n%s'
        client.set_debuglevel(1)
        client.sendmail(sender,dest,message_template%(sender,dest,message))
        client.quit()
        print("-Email enviado con exito")

    def enviarFTP(self):
        print("\n-Conectando por ftp ...")
        server = "192.168.1.123"
        port = 23
        user = "dostres"
        password = "dostresdos"
        local_file_path = "archivo_descifrado.txt"
        remote_file_path = "/archivo_descifradoAlexTesan.txt"

        # Crear conexión FTP
        ftp = FTP()
        ftp.connect(server, port)
        ftp.login(user, password)

        self.MostrarDirectoriosFTP(ftp)
        print("Subiendo archivo ...")

        with open(local_file_path, "rb") as file:
            ftp.storbinary(f"STOR {remote_file_path}", file)        # Subir el archivo al servidor FTP

        self.MostrarDirectoriosFTP(ftp)
        ftp.quit()

        print("Archivo enviado correctamente al servidor FTP.")

    def ejecutar_comando(self, ssh, comando):
        stdin, stdout, stderr = ssh.exec_command('cd {}; {}'.format(self.directorio_actual, comando))
        return stdout.readlines()

    def MostrarDirectoriosSSH(self, ssh):      # Ejecutar el comando "ls"
        lines = self.ejecutar_comando(ssh, 'ls')
        print('-Archivos y directorios en el servidor:')
        for line in lines:
            print(line.strip())

    def MostrarDirectorioActualSSH(self, ssh): # Ejecutar el comando "pwd"
        lines = self.ejecutar_comando(ssh, 'pwd')
        print('-Directorio actual en el servidor:')
        for line in lines:
            print(line.strip())

    def MostrarDirectoriosFTP(self, ftp):
        print('-Archivos y directorios en el servidor:')
        files = ftp.nlst()
        for file in files:
            print(file)

    def CambiarDirectorioSSH(self, ssh, nuevo_directorio):
        self.directorio_actual = nuevo_directorio
        print('-Cambiando al directorio:', nuevo_directorio)

    def iniciarServidorHTTP(self):
        class HTTPRequestHandler(BaseHTTPRequestHandler):
            def do_HEAD(self):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

            def do_GET(self):
                self.do_HEAD()
                self.wfile.write("""<html><head><title>Hello World</title></head><body><p>Hello World</p><form method="POST" ><input type="submit" value="Click me" /></form></body></html>""".encode("utf-8"))

            def do_POST(self):
                self.do_HEAD()
                pr = Principal()
                pr.conexionSSH()
                self.wfile.write("""<html><head><title>Resultado</title></head><body><p>Examen completado</p></body></html>""".encode("utf-8"))

        server_address = ('localhost', 8083)
        httpd = HTTPServer(server_address, HTTPRequestHandler)
        print('Servidor HTTP iniciado en el puerto 8083...')
        httpd.serve_forever()

    def passTheExam(self):
        print("Examen completado con éxito.")

if __name__ == "__main__":
    pr = Principal()
    pr.pasos()
