from ftplib import FTP

# Configuración de la conexión FTP
ftp = FTP('localhost')
ftp.login(user='admin', passwd='preguntaraalberto')

try:
    # Listar archivos en el servidor
    print("Archivos en el servidor:")
    files = ftp.nlst()
    for file in files:
        print(file)

    # Descargar un archivo
    filename = 'my_file.txt'
    with open(filename, 'wb') as f:
        ftp.retrbinary('RETR ' + filename, f.write)

    print(f"Archivo '{filename}' descargado.")

    # Leer el contenido del archivo descargado
    with open(filename, 'r') as f:
        print(f"Contenido de '{filename}':")
        print(f.read())

except Exception as e:
    print("Error:", e)

finally:
    # Cerrar la conexión FTP
    ftp.quit()


    """ftp.cwd('/') #desplazarse en el arbol
    print(ftp.pwd()) # saber en que carpeta esta
    print(ftp.getwelcome())"""