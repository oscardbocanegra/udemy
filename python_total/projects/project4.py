from random import randint

intentos = 0
numero_secreto =randint(1, 100)
name = input("Cual es tu nombre: ")
print(f"Bueno{name}, he pensado en un numero entre 1 y 100 \nTienes 8 intentos para adivinar")

while intentos < 8:
    estimado = int(input("Cual es el numero?: "))
    intentos += 1
    
    if estimado < numero_secreto:
        print("Mi numero es mas alto")
        
    elif estimado > numero_secreto:
        print("Mi numero es mas bajo")
        
    elif estimado == numero_secreto:
        print(f"Felicitaciones {name}! Has adivinado en {intentos} intentos")
        break
if estimado != numero_secreto:
    print(f"Lo sentimos, se han agotado los intentos,    el numero secreto era {numero_secreto}")
