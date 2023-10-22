"""Ejercicio 12: Crea una clase llamada Cuenta que tendrá los siguientes atributos: 
titular y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional.
Crea sus métodos get, set y toString. Tendrá dos métodos especiales:
    - ingresar(double cantidad): se ingresa una cantidad a la cuenta si la cantidad
    introducida es negativa, no se hará nada.
    - retirar(double cantidad): se retira una cantidad a la cuenta, si restando la 
    cantidad actual a la que nos pasan es negativa, la cantidad de la cuenta pasa a ser 0."""


class Cuenta:
    def __init__(self, titular, cantidad=0.00):
        self.titular = titular
        self.cantidad = cantidad
        
    def getTitular(self):
        return self.titular
    
    def setTitular(self, titular):
        self.titular = titular
        
    def getCantidad(self):
        return self.cantidad
    
    def setCantidad(self, cantidad):
        if cantidad >= 0:
            self.cantidad = cantidad
        
    def toString(self):
        return f"Titular: {self.titular}, Saldo: {self.cantidad:.2f}€"
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
            
    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad
            if self.cantidad < 0:
                self.cantidad = 0


cuenta = Cuenta("María", 100.00)
print(cuenta.toString())

cuenta.ingresar(50.00)
print(cuenta.toString())

cuenta.retirar(25.00)
print(cuenta.toString())

cuenta.retirar(200.00)
print(cuenta.toString())