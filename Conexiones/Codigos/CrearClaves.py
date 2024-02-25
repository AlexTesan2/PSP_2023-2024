from Crypto.PublicKey import RSA

# Generar un par de claves RSA de 2048 bits
key = RSA.generate(2048)


with open("clavePublica.pem", "wb") as archivo_publico:               # Guardar la clave pública en un archivo
    archivo_publico.write(key.publickey().export_key())               #Sirve para encriptar

with open("clavePrivada.pem", "wb") as archivo_privado:               # Guardar la clave privada en un archivo
    archivo_privado.write(key.export_key())                           #Sirve para desencriptar

print('claves generadas correctamente')
