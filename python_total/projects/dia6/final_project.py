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

def mostrar_categoria(ruta):
    print("Categorias:")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1
    
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f'[{contador}] - {carpeta_str}')
        lista_categorias.append(carpeta)
        contador += 1
    
    return lista_categorias

def elgir_categoria(lista):
    eleccion_correcta = 'x'
    
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\nElige una categoria: ")
        
    return lista[int(eleccion_correcta) - 1]

def mostrar_recetas(ruta):
    print("recetas: ")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1
    
    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas

def elegir_recetas(lista):
    eleccion_receta = 'x'
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista)+1):
        eleccion_receta = input("\nElige una receta: ")
        
    return lista[int(eleccion_receta) -1]

menu = 0

if menu == 1:
    mis_categorias = mostrar_categoria(mi_ruta)
    mi_categoria = elgir_categoria(mis_categorias)
    mis_recetas = mostrar_recetas(mi_categoria)

elif menu == 2:
    mis_categorias = mostrar_categoria(mi_ruta)
    mi_categoria = elgir_categoria(mis_categorias)

elif menu == 3:
    pass

elif menu == 4:
    mis_categorias = mostrar_categoria(mi_ruta)
    mi_categoria = elgir_categoria(mis_categorias)
    mis_recetas = mostrar_recetas(mi_categoria)

elif menu == 5:
    mis_categorias = mostrar_categoria(mi_ruta)
    mi_categoria = elgir_categoria(mis_categorias)

elif menu == 6:
    pass