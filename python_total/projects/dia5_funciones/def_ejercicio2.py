#Práctica sobre Interacción entre Funciones 2: Crea una función llamada reducir_lista() 
#que tome una lista como argumento (crea también la variable lista_numeros), y devuelva 
#la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) 
#y eliminando el valor más alto. El orden de los elementos puede modificarse. Crea una función 
#llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, 
#y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.

lista_numeros = [1,2,15,7,2,8]
 
def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista
 
def promedio(lista):
    valor_medio = sum(lista)/len(lista)
    return valor_medio
