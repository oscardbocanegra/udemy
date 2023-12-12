def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def contar_primos(numero):
    primos_encontrados = []
    for i in range(2, numero + 1):
        if es_primo(i):
            primos_encontrados.append(i)
            print(i, end=' ')
    
    print("\nCantidad de números primos encontrados:", len(primos_encontrados))
    return len(primos_encontrados)

# Ejemplo de uso:
limite_superior = 20
cantidad_primos = contar_primos(limite_superior)
