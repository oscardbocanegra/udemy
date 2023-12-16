import os
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(), "udemy", "python_total", "projects", "dia6" ,"recetas")

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador

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