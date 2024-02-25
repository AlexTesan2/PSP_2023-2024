import paramiko
from scp import SCPClient
import smtplib
import os
from email.mime.text import MIMEText
from ftplib import FTP
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class Principal():
    def pasos(self):
        self.conexionSSH()
        self.descifrar()
        self.enviarCorreo()
        self.enviarFTP()

    def conexionSSH(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(hostname='localhost', port=2222, username='linuxserver', password='password')
            print("-Conectado por SSH...")

            self.MostrarDirectorioActualSSH(ssh)
            self.MostrarDirectoriosSSH(ssh)

            scp = SCPClient(ssh.get_transport())
            scp.get('archivo_encriptado.txt')                     # Descargar el archivo
            scp.get('clavePrivada.pem')
            scp.close()

            """# Leer el archivo después de descargarlo
            with open('sshd.pid', 'r') as file:
                print("Contenido del archivo:")
                print(file.read())"""

        #Posibles excepciones
        except paramiko.AuthenticationException:
            print("Error de autenticación. Asegúrate de que las credenciales sean correctas.")
        except paramiko.SSHException as e:
            print("Error de conexión SSH:", e)
        finally:
            ssh.close()

    def descifrar(self):
        print("\ndescifrar")

        with open("clavePrivada.pem", "rb") as key_file:
            private_key_data = key_file.read()
        
        private_key = RSA.import_key(private_key_data)

        with open("archivo_encriptado.txt", "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()

        # Descifrado utilizando la clave privada
        cipher_rsa = PKCS1_OAEP.new(private_key)
        decrypted_data = cipher_rsa.decrypt(encrypted_data)

        # Escribir datos descifrados en un nuevo archivo
        with open("archivo_descifrado.txt", "wb") as decrypted_file:
            decrypted_file.write(decrypted_data)

        print("Archivo descifrado con éxito.")


    def enviarCorreo(self):
        print("\n-enviando Correo ...")
        client= smtplib.SMTP(host='localhost',port=1025)
        sender= 'tesan.deale22@zaragoza.salesianos.edu'
        dest='ventura.tocar22@zaragoza.salesianos.edu'
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
        server = "localhost"
        port = 21
        user = "admin"
        password = "preguntaraalberto"
        local_file_path = "archivo_descifrado.txt"
        remote_file_path = "/archivo_descifrado3.txt"

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
    


    def MostrarDirectoriosSSH(self, ssh):      # Ejecutar el comando "ls"
        stdin, stdout, stderr = ssh.exec_command('ls') 
        print('-Archivos y directorios en el servidor:')
        for line in stdout:
            print(line.strip())

    def MostrarDirectorioActualSSH(self, ssh): # Ejecutar el comando "pwd"
        stdin, stdout, stderr = ssh.exec_command('pwd') 
        print('-Directorio actual en el servidor:')
        for line in stdout:
            print(line.strip())
    
    def CambiarDirectorioSSH(self, ssh, nuevo_directorio):  # Ejecutar el comando "cd"
        stdin, stdout, stderr = ssh.exec_command('cd ' + nuevo_directorio) 
        print('-Cambiando al directorio:', nuevo_directorio)
        for line in stdout:
            print(line.strip())
    #self.CambiarDirectorioSSH(ssh, 'ssh_host_keys')
    
    def MostrarDirectoriosFTP(self, ftp):
        print('-Archivos y directorios en el servidor:')
        files = ftp.nlst()
        for file in files:
            print(file)


pr = Principal()
pr.pasos()
