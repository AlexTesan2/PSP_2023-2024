import paramiko
from scp import SCPClient

# Establecer la conexión SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(hostname='localhost', port=2222, username='linuxserver', password='password')
    print('Conectado por SSH')

    # Ejecutar el comando "ls" para mostrar los archivos y directorios
    stdin, stdout, stderr = ssh.exec_command('ls')
    print('Archivos y directorios en el servidor:')
    for line in stdout:
        print(line.strip())

    scp = SCPClient(ssh.get_transport())
    scp.get('sshd.pid')                     # Descargar el archivo
    scp.close()

    # Leer el archivo después de descargarlo
    with open('sshd.pid', 'r') as file:
        print("Contenido del archivo:")
        print(file.read())

except paramiko.AuthenticationException:
    print("Error de autenticación. Asegúrate de que las credenciales sean correctas.")
except paramiko.SSHException as e:
    print("Error de conexión SSH:", e)
finally:
    ssh.close()

