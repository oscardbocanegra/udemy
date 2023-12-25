#Práctica Polimorfismo 1: La función incorporada en Python len() tiene un comportamiento polimórfico, ya que calcula el 
#largo de un objeto en función de su tipo (strings, listas, tuples, entre otros), devolviendo la cantidad de items o 
#caracteres que lo componen. Crea un iterador que recorra los siguientes objetos: palabra, lista, tupla y muestre en 
#pantalla (print()) para cada uno de ellos su longitud con la función len().

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

for dato in [palabra, lista, tupla]:
    print(len(dato))
    
#Práctica Polimorfismo 2: Cuentas con tres clases de personajes en un juego, los cuales cuentan con sus métodos de ataque 
#específicos. Crea un iterador que logre un ataque conjugado en el siguiente orden: Arquero, Mago, Samurai, llamando al 
#método atacar() de cada uno de los personajes. Deberás crear instancias de cada una de las clases anteriores para construir 
#un iterable (una lista llamada personajes) que pueda recorrese en dicho orden.

class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")
        
personaje1 = Mago()
personaje2 = Arquero()
personaje3 = Samurai()

personajes = [personaje2, personaje1, personaje3]

for personaje in personajes:
    personaje.atacar()
    
#Práctica Polimorfismo 3: Tienes tres clases de personajes en un juego, los cuales cuentan con sus métodos de 
#defensa específicos.Crea una función llamada personaje_defender(), que pueda recibir un objeto (una instancia 
#de las clases de tus personajes), y ejecutar su método defender() independientemente de qué tipo de personaje se trate.

class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

def personaje_defender(personaje):
    personaje.defender()