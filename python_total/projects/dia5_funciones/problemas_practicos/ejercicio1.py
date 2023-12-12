def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    if suma >= 15:
        print(f"El valor es mayor a 15: {suma}")
        return max(num1, num2, num3)
    elif suma < 10:
        print(f"El valor es menor a 10: {suma}")
        return min(num1, num2, num3)
    elif suma >= 10 and suma <= 15:
        print(f"El valor esta entre 10 y 15: {suma}")
        return suma - max(num1, num2, num3) - min(num1, num2, num3)
        
              
valores = devolver_distintos(15, 5, 1)
print(valores)