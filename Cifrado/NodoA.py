import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Dirección IP y puerto del nodo B
HOST = '192.168.50.1'
PORT = 5000

# Cargar la clave pública de B
with open('public_key.pem', 'rb') as f:
    public_key = RSA.import_key(f.read())

# Establecer conexión con el nodo B
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Encriptar el archivo utilizando la clave pública de B
    cipher_rsa = PKCS1_OAEP.new(public_key)
    with open('mensaje.txt', 'rb') as f:
        file_data = f.read()
        encrypted_data = cipher_rsa.encrypt(file_data)

    # Transmitir el archivo encriptado
    s.sendall(encrypted_data)

print("Archivo enviado correctamente")
