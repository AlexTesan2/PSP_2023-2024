from ftplib import FTP
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

server = "localhost"
port = 21
user = "admin"
password = "preguntaraalberto"
local_file_path = "texto.txt"
remote_file_path = "/my_file.txt"

# Cargar clave pública
with open("clavePublica.pem", "rb") as public_key_file:
    public_key = RSA.import_key(public_key_file.read())

# Encriptar archivo utilizando la clave pública
with open(local_file_path, "rb") as file:
    data = file.read()
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_data = cipher.encrypt(data)

# Subir archivo encriptado al servidor FTP
with FTP() as ftp:
    ftp.connect(server, port)
    ftp.login(user, password)

    with open("archivo_encriptado.txt", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    
    # Abre el archivo en modo lectura antes de pasarlo a storbinary
    with open("archivo_encriptado.txt", "rb") as encrypted_file:
        ftp.storbinary("STOR /archivo_encriptado.txt", encrypted_file)

    # Subir clave privada al servidor FTP
    with open("clavePrivada.pem", "rb") as private_key_file:
        ftp.storbinary("STOR /clavePrivada.pem", private_key_file)
    
    print('-Archivos y directorios en el servidor:')
    files = ftp.nlst()
    for file in files:
        print(file)

    print("Archivos enviados correctamente al servidor FTP.")
    ftp.quit()



























"""from ftplib import FTP

server = "localhost"
port = 21
user = "admin"
password = "preguntaraalberto"
local_file_path = "texto.txt"
remote_file_path = "/my_file.txt"

# Crear conexión FTP
ftp = FTP()
ftp.connect(server, port)
ftp.login(user, password)


with open(local_file_path, "rb") as file:
    ftp.storbinary(f"STOR {remote_file_path}", file)        # Subir el archivo al servidor FTP


files = ftp.nlst()
for file in files:
    print(file)

ftp.quit()

print("Archivo enviado correctamente al servidor FTP.")"""