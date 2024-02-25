import paramiko
from scp import SCPClient

# Datos de conexión SSH
local_file_path = "texto.txt"
remote_file_path = "/logs/my_file2.txt"

# Conexión SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(hostname='localhost', port='2222', username='linuxserver', password='password')
    print('Conexión SSH establecida.')
    
    # Subir archivo al servidor
    scp = SCPClient(ssh.get_transport())
    
    scp.put('clavePrivada.pem')
    scp.put('archivo_encriptado.txt')

    # Listar archivos en el servidor
    stdin, stdout, stderr = ssh.exec_command('ls') 
    print('-Archivos y directorios en el servidor:')
    for line in stdout:
        print(line.strip())
    print('Archivo enviado al servidor.')


    scp.close()

except paramiko.AuthenticationException:
    print("Error de autenticación. Asegúrate de que las credenciales sean correctas.")
except paramiko.SSHException as e:
    print("Error de conexión SSH:", e)
finally:
    # Cerrar conexión SSH
    ssh.close()
