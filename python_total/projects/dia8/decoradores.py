def decorar_saludo(funcion):
    
    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('Adios')
        
    return otra_funcion

def mayuscula(texto):
    print(texto.upper())
    
def minuscula(texto):
    print(texto.lower())
    
mayuscula_decorada = decorar_saludo(mayuscula)
mayuscula_decorada("Python")