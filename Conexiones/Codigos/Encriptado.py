from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

def encrypt_file(archivo, clave):

    session_key = os.urandom(16)                                    # Generar una clave

    public_key = RSA.import_key(open("clavePublica.pem").read())    # Importar la clave pública RSA desde el archivo
    cipher_rsa = PKCS1_OAEP.new(public_key)

    enc_session_key = cipher_rsa.encrypt(session_key)               # Encriptar la clave de sesión con RSA

    with open(clave, 'wb') as clave:                                # Escribir la clave encriptada al archivo
        clave.write(enc_session_key)

    with open(archivo, 'rb') as file_in:                            # Leer el contenido del archivo
        file_data = file_in.read()

    encrypted_data = cipher_rsa.encrypt(file_data)                  # Encriptar el contenido del archivo con RSA

    with open(archivo + ".enc", 'wb') as encrypted_file:            # Escribir el archivo encriptado
        encrypted_file.write(encrypted_data)

    print("Archivo encriptado y clave guardada.")

archivo = "texto.txt"
clave = "key.bin"
encrypt_file(archivo, clave)
print('fin')
