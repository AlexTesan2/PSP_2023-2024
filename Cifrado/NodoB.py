import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Puerto para escuchar conexiones
PORT = 5000

# Cargar la clave privada de B
with open('private_key.pem', 'rb') as f:
    private_key = RSA.import_key(f.read())

# Establecer el servidor socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', PORT))
    s.listen()

    conn, addr = s.accept()
    with conn:
        print('Conectado por', addr)
        encrypted_data = conn.recv(4096)

        # Desencriptar el archivo utilizando la clave privada de B
        cipher_rsa = PKCS1_OAEP.new(private_key)
        decrypted_data = cipher_rsa.decrypt(encrypted_data)

        # Guardar el archivo desencriptado
        with open('archivo_recibido.txt', 'wb') as f:
            f.write(decrypted_data)

print("Archivo recibido y desencriptado correctamente")
