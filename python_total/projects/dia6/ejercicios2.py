#Práctica Crear y Escribir Archivos 1: Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".
#Imprime el contenido completo de "mi_archivo.txt" al finalizar.

archivo = open("mi_archivo.txt", "w")
archivo.write("Nuevo texto")
archivo.close()

archivo = open("mi_archivo.txt", "r")
print(archivo.read())

#Práctica Crear y Escribir Archivos 2: Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".
#Imprime el contenido completo de "mi_archivo.txt" al finalizar. Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.

archivo = open("mi_archivo.txt", "a")
archivo.write("Nuevo inicio de sesión")
archivo.close()

archivo = open("mi_archivo.txt", "r")
print(archivo.read())

#Práctica Crear y Escribir Archivos 3: Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo 
#"registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.
#registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]Imprime el contenido completo de "registro.txt" al finalizar.

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
 
registro = open("registro.txt","a")
for item in registro_ultima_sesion:
    registro.writelines(item +'\t')
 
registro.close()
registro = open("registro.txt","r")
print(registro.read())