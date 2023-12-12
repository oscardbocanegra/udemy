def orden(frase):
    fra = set(frase)
    ordenada = ''.join(sorted(fra))
    return ordenada

palabra = "entretenido"
total = orden(palabra)
print(total)