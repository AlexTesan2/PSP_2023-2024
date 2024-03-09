
# No es necesario para que funcione ejercicio1.py  !!!!!!!!!!!!!!!!
nombre_archivo = 'file.txt'


with open(nombre_archivo, 'w') as archivo:
    archivo.write('Hola, este es un nuevo archivo creado con Python.\n')
    archivo.write('Puedes agregar más líneas si lo deseas.\n')


print(f'Se ha creado el archivo: {nombre_archivo}')
