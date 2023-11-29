#Los vendedores reciben comisiones del 13% por sus ventas totales, calcular las comiciones preguntando el nombre y cunto han vendido 

nombre = input("Cual es tu nombre? ")
ventas = float(input("Cuanto has vendido en el ultimo mes? "))
porcentaje = ventas * 13 / 100
total = print(f"ok {nombre}, este mes ganaste {porcentaje}")