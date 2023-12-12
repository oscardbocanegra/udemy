def verificar_cero_consecutivo(*args):
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i + 1] == 0:
            return True
    return False

resultado1 = verificar_cero_consecutivo(5, 6, 1, 0, 0, 9, 3, 5)
print(resultado1)  # Devuelve True

resultado2 = verificar_cero_consecutivo(6, 0, 5, 1, 0, 3, 0, 1)
print(resultado2)  # Devuelve False
