# 🚗 Ejercicio propuesto: Sistema de pago para una tienda online
# 🎯 Objetivo:
# Implementar un sistema de pagos utilizando el principio de inversión de dependencias (DIP).

# 🧩 Requisitos:
# El sistema puede procesar pagos mediante:

# Tarjeta de crédito

# PayPal

# Criptomonedas

# El sistema de pagos NO debe depender directamente de las implementaciones específicas.

# 📝 Instrucciones:
# Crea una interfaz o clase abstracta llamada PaymentMethod con un método pay(amount: float).

# Crea las implementaciones específicas:

# CreditCardPayment

# PayPalPayment

# CryptoPayment

# Crea un sistema de pagos de alto nivel (PaymentProcessor) que dependa de la abstracción PaymentMethod, no de las clases concretas.

# Crea un pequeño ejemplo donde se vea:

# Una versión incorrecta del diseño (violando DIP)

# Una versión correcta (siguiendo DIP)

from abc import ABC, abstractmethod

# #VERSION INCORRECTA DE DIP

# class pago(ABC):
#     @abstractmethod
#     def monto(self,monto:float):
#         pass
#     @abstractmethod
#     def wallet(self,id:int):
#         pass


# class PayPal(pago):
#     def monto(self,monto:float):
#         print(monto)
    
#     ## paypal no tiene wallet a difernecia de las crypto porlo que este seria un ejemplo de violacion de dip
#     ## una dependencia no abstracta de las clases  CreditCardPayment PayPalPayment CryptoPayment de pago 



# VERSION CORRECTA DE DIP

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount:float):
        pass

class CreditCardPayment(PaymentMethod):
    def pay(self,amount:float):
        print(f"Targeta Aceptada Monto: ${amount}")

class PayPalPayment(PaymentMethod):
    def pay(self,amount:float):
        print(f"PayPal Aceptada Monto: ${amount}")

class CryptoPayment(PaymentMethod):
    def pay(self,amount:float):
        print(f"Wallet Aceptada Monto: ${amount}")


class sendPayment:
    def __init__(self,method:PaymentMethod):
        self.method = method

    def sendIt(self,monto:float):
        self.method.pay(monto)


sendPayment(CreditCardPayment()).sendIt(5.0)
sendPayment(CryptoPayment()).sendIt(5.0)
sendPayment(PayPalPayment()).sendIt(5.0)