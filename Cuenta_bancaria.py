class CuentaBancaria:
    def __init__(self):
        self.__saldo = 0  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Saldo actual: {self.__saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que 0.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Saldo actual: {self.__saldo}")
        else:
            print("No hay suficiente saldo o cantidad inválida.")

    def obtener_saldo(self):
        return self.__saldo

# Ejemplo de uso
cuenta = CuentaBancaria()
cuenta.depositar(5000)  # Depósito
cuenta.retirar(500)     # Retiro
print(f"Saldo disponible: {cuenta.obtener_saldo()}")  # Consultar saldo