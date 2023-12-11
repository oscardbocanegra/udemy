#Práctica Funciones Dinámicas 2: Crea una función (suma_menores)
#que sume los números de una lista (almacenada en la variable lista_numeros) 
#siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado 
#de dicha suma.

lista_numeros = [1, 2, 3, 4, 5, 6]

def suma_menores(numeros):
    
    suma = 0 
    
    for i in numeros:
        if i in range(0, 1001):
            suma += i
        else:
            pass
    return suma
    
total = suma_menores(lista_numeros)
print("total ejercicio 1 = ",total)

#Práctica Funciones Dinámicas 3: Crea una función (cantidad_pares) que 
#cuente la cantidad de números pares que existen en una lista 
#(lista_numeros), y devuelva el resultado de dicha cuenta.

lista_numeros = [1, 2, 3, 4, 5, 6, 7]

def cantidad_pares(numeros):
    suma = 0
    for i in numeros:
        if i % 2 == 0:
            suma += 1
        else:
            pass
    return suma
    
total2 = cantidad_pares(lista_numeros)
print("total ejercicio 2 = ", total2)