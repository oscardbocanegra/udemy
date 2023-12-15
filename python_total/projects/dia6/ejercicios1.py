# Práctica Abrir y Manipular Archivos 1: Abre el archivo texto.txt e imprime su contenido. 
archivo = open('texto.txt')

print(archivo.read())

print("************************************")
#Práctica Abrir y Manipular Archivos 1: Abre el archivo texto.txt e imprime su contenido.
print("\nThis is the 2nd excercise on this test\n")
archivo = open('texto.txt')

print(archivo.readline())
print("************************************")

#Práctica Abrir y Manipular Archivos 3: Abre el archivo texto.txt e imprime únicamente la segunda línea.

print("\nThis is the 3rd excercise on this test\n")

archivo = open("texto.txt")
lineas = archivo.readlines()
print(lineas[1])

archivo.close()