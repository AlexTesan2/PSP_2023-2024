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
        self.conexionFTP()
        self.descifrar()
        self.enviarCorreo()
        self.enviarSSH()

    def conexionFTP(self):
        print("conectando por FTP ...")
        ftp = FTP('localhost')
        ftp.login(user='admin', passwd='preguntaraalberto')

        try:
            self.MostrarDirectoriosFTP(ftp)

            # Descargar un archivo
            filename = 'archivo_encriptado.txt'
            clave= 'clavePrivada.pem'

            with open(filename, 'wb') as f:
                ftp.retrbinary('RETR ' + filename, f.write)
            
            with open(clave, 'wb') as c:
                ftp.retrbinary('RETR ' + clave, c.write)

            print(f"Archivo '{filename}' y clave descargados.")

            # Leer el contenido del archivo descargado
            """with open(filename, 'r') as f:
                print(f"Contenido de '{filename}':")
                print(f.read())"""

        except Exception as e:
            print("Error:", e)

        finally:
            # Cerrar la conexión FTP
            ftp.quit()

    def descifrar(self):
        print("\ndescifrar")

        # Lectura de la clave privada desde el archivo
        with open("clavePrivada.pem", "rb") as key_file:
            private_key_data = key_file.read()
        # Carga de la clave privada
        private_key = RSA.import_key(private_key_data)

        # Lectura del archivo encriptado
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


    def enviarSSH(self):
        # Conexión SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(hostname='localhost', port=2222, username='linuxserver', password='password')
            print('\n-Conexión SSH establecida.')

            self.MostrarDirectorioActualSSH(ssh)
            self.MostrarDirectoriosSSH(ssh)
            # Subir archivo al servidor
            
            scp = SCPClient(ssh.get_transport())
            scp.put('archivo_descifrado.txt', 'archivo_descifrado.txt')

            self.MostrarDirectoriosSSH(ssh)
            print('Archivo enviado al servidor.')
            scp.close()

        except paramiko.AuthenticationException:
            print("Error de autenticación. Asegúrate de que las credenciales sean correctas.")
        except paramiko.SSHException as e:
            print("Error de conexión SSH:", e)
        finally:
            # Cerrar conexión SSH
            ssh.close()

    

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


    def MostrarDirectoriosFTP(self, ftp):
        print('-Archivos y directorios en el servidor:')
        files = ftp.nlst()
        for file in files:
            print(file)


pr = Principal()
pr.pasos()