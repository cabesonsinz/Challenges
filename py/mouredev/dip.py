# *
#  * EJERCICIO:
#  * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
#  * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
#  * de forma correcta e incorrecta.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un sistema de notificaciones.
#  * Requisitos:
#   * 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
#  * 2. El sistema de notificaciones no puede depender de las implementaciones específicas.  * Instrucciones:
#  * 1. Crea la interfaz o clase abstracta.
#   * 2. Desarrolla las implementaciones específicas.
#   * 3. Crea el sistema de notificaciones usando el DIP.
#   * 4. Desarrolla un código que compruebe que se cumple el principio.


from abc import ABC,abstractmethod

## DIP EL ALTO NIVEL Y BAJO DEBEN TENER LA MENOR DEPENDECIA POSIBLE 


## REGLAS DE NEGOCIO  ALTO NIVEL
class ITmessages(ABC):

    @abstractmethod
    def message(self,message:str):
        pass
    

class emailMessage(ITmessages):
    def message(self,realMessage:str):
        return(f"Email-Message = {realMessage}  ")

class pushMessage(ITmessages):
    def message(self,realMessage:str):
        return(f"Push-Message = {realMessage}  ")

class smsMessage(ITmessages):
    def message(self,realMessage:str):
        return(f"Sms-Message = {realMessage} ")




## PROCESOS BAJO NIVEL


class notifier:
    def __init__(self,type:ITmessages) -> None:
        self.type = type

    def sendIt(self,realMessage:str):
        print(self.type.message(realMessage))



service = notifier(smsMessage())

service.sendIt("ASd")

