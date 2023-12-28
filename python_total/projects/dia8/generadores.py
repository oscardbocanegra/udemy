#Práctica Generadores 1: Crea un generador (almacenado en la variable generador)
#que sea capaz de devolver una secuencia infinita de números, iniciando desde el 1,
#y entregando un número consecutivo superior cada vez que sea llamada mediante next.
def secuencia_infinita():
    num = 0
    while True:
        num += 1
        yield num
 
generador = secuencia_infinita()

#Práctica Generadores 2: Crea un generador (almacenado en la variable generador) que sea
#capaz de devolver de manera indefinida múltiplos de 7, iniciando desde el mismo 7, y que 
# cada vez que sea llamado devuelva el siguiente múltiplo (7, 14, 21, 28...).

def multiplos_siete():
    num = 1
    while True:
        yield 7*num
        num += 1
 
generador = multiplos_siete()

#Práctica Generadores 3: Crea un generador que reste una a una las vidas de un personaje de
#videojuego, y devuelva un mensaje cada vez que sea llamado: "Te quedan 3 vidas", "Te quedan 2 vidas"
#"Te queda 1 vida", "Game Over", Almacena el generador en la variable perder_vida

def mensaje():
    x = "Te quedan 3 vidas"
    yield x
    
    x = "Te quedan 2 vidas"
    yield x
 
    x = "Te queda 1 vida"
    yield x
    
    x = "Game Over"
    yield x
 
perder_vida = mensaje()
