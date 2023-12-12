#Práctica sobre Interacción entre Funciones 3: Crea una función (llamada lanzar_moneda)
#que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe poder devolver 
#los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.
#Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, 
# debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de 
#números cualquiera (debes crear una lista con valores y llamarla lista_numeros).
#Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", 
#y eliminarla (devolverla como lista vacía []).
#Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.

from random import choice

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def lanzar_moneda():
    moneda = (["Cara", "Cruz"])
    moneda = choice(moneda)
    return moneda
    
def probar_suerte(lanzamiento, lista):
    if lanzamiento == 'Cara':
        lista = lista.pop()
        print("La lista se autodestruirá")
        return []
    else:
        print(f"La lista fue salvada")
        return lista
        
lanzamiento = lanzar_moneda()
suerte = probar_suerte(lanzamiento, lista_numeros)
print(suerte)

