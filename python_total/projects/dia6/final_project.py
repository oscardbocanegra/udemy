import os
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(), "udemy", "python_total", "projects", "dia6" ,"recetas")

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador

def inicio():
    system('clear')
    print("*" * 50)
    print('*' * 5 ," Bienvenido al administrador de recetas ", '*' * 5)
    print("*" * 50)
    print("\n")
    print(f"Las recetas se encuentran en: {mi_ruta}")
    print(f"Total recetas: {contar_recetas(mi_ruta)}")
    
    
    eleccion_menu = "x"
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opcion")
        print("""
              [1] - Leer receta
              [2] - Crear receta nueva
              [3] - Crear categoria nueva
              [4] - Eliminar receta
              [5] - Eliminar categoria
              [6] - Salir del programa""")
        eleccion_menu = input()
    return (eleccion_menu)
    
inicio()



menu = 0

if menu == 1:
    pass

elif menu == 2:
    pass

elif menu == 3:
    pass

elif menu == 4:
    pass

elif menu == 5:
    pass

elif menu == 6:
    pass