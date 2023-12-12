#Práctica sobre Interacción entre Funciones 1
#Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:La 
#función debe retornar dos valores resultado, que se encuentren entre 1 y 6).Dicha función 
#no debe requerir argumentos para funcionar, sino que debe generar internamente los valores 
#aleatorios.Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada 
#(es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- 
#un mensaje según la suma de estos valores:Si la suma es menor o igual a 6:"La suma de tus dados 
#es {suma_dados}. Lamentable" Si la suma es mayor a 6 y menor a 10: "La suma de tus dados es 
#{suma_dados}. Tienes buenas chances" Si la suma es mayor o igual a 10: "La suma de tus dados 
#es {suma_dados}. Parece una jugada ganadora"

from random import randint

def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    total = dado1 + dado2
    return total
    
def evaluar_jugaada(jugada):
    if jugada <= 6:
        print(f"La suma de tus dados es {jugada}. Lamentable")
    elif jugada > 6 and jugada < 10:
        print(f"La suma de tus dados es {jugada}. Tienes buenas chances")
    elif jugada >= 10:
        print(f"La suma de tus dados es {jugada}. Parece una jugada ganadora")
    
    
jugada = lanzar_dados()
evaluar = evaluar_jugaada(jugada)

