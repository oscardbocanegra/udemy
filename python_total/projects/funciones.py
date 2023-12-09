#Práctica Return 1: Crea una función llamada potencia 
#que tome dos valores numéricos como argumentos. Deberá 
#devolver el número que resulte de resolver una potencia, 
#utilizando el primer número como base, y el segundo como exponente

def potencia(numero1, numero2):
    return numero1**numero2
    
result = potencia(3,4)
print(result)

#Práctica Return 2:
#Crea una función llamada usd_a_eur que tome como único parámetro 
#un valor numérico (un monto en dólares estadounidenses), y devuelva
#como resultado el monto equivalente en euros. A fines de este ejemplo, 
#tomaremos la conversión 1 USD = 0.90 EUR./ 2.Crea una variable llamada 
#dolares y almacena en ella un monto cualquiera para entregárselo a tu función 
#y evaluar su resultado.
dolares = 2000

def usd_a_eur(num):
    return num * 0.90
    
conversion = usd_a_eur(dolares)
print(conversion)