class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0.0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def imprimir_cliente(self):
        print(f"Cliente: {self.nombre} {self.apellido}, Cuenta: {self.numero_cuenta}, Balance: ${self.balance}")

    def depositar(self, monto):
        self.balance += monto
        print(f"Depósito realizado. Nuevo balance: ${self.balance}")

    def retirar(self, monto):
        if monto <= self.balance:
            self.balance -= monto
            print(f"Retiro realizado. Nuevo balance: ${self.balance}")
        else:
            print("Saldo insuficiente.")

cliente1 = Cliente(nombre="Oscar", apellido="Bocanegra", numero_cuenta="123456", balance=1000.0)

while True:
    print("\n1. Imprimir Cliente\n2. Depositar\n3. Retirar\n4. Salir")
    opcion = input("Elija una opción (1-4): ")

    if opcion == "1":
        cliente1.imprimir_cliente()
    elif opcion == "2":
        monto_deposito = float(input("Ingrese el monto a depositar: "))
        cliente1.depositar(monto_deposito)
    elif opcion == "3":
        monto_retiro = float(input("Ingrese el monto a retirar: "))
        cliente1.retirar(monto_retiro)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, elija una opción válida.")
