from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def decrypt_file(archivo_encriptado, clave, archivo_desencriptado):
    
    with open(clave, 'rb') as clave_archivo:
        enc_session_key = clave_archivo.read()

    private_key = RSA.import_key(open("clavePrivada.pem").read())  # Importar la clave privada RSA desde el archivo
    cipher_rsa = PKCS1_OAEP.new(private_key)

    session_key = cipher_rsa.decrypt(enc_session_key)              # Desencriptar la clave de sesión con RSA

    with open(archivo_encriptado, 'rb') as file_in:                # Leer el contenido del archivo encriptado
        encrypted_data = file_in.read()

    decrypted_data = cipher_rsa.decrypt(encrypted_data)           # Desencriptar el contenido del archivo con RSA

    with open(archivo_desencriptado, 'wb') as desencriptado_file: # Escribir el archivo desencriptado
        desencriptado_file.write(decrypted_data)

    print("Archivo desencriptado.")
    print(decrypted_data)

archivo_encriptado = "texto.txt.enc"
clave = "key.bin"
archivo_desencriptado = "texto_desencriptado.txt"

decrypt_file(archivo_encriptado, clave, archivo_desencriptado)
print('fin')

