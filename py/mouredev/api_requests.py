
# /*
#  * EJERCICIO:
#  * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
#  * una petición a la web que tú quieras, verifica que dicha petición
#  * fue exitosa y muestra por consola el contenido de la web.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
#  * terminal al que le puedas solicitar información de un Pokémon concreto
#  * utilizando su nombre o número.
#  * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
#  * - Muestra el nombre de su cadena de evoluciones
#  * - Muestra los juegos en los que aparece
#  * - Controla posibles errores
#  */



# try:
#     page = requests.get("https://web.dragonball-api.com/")

# except Exception as error:
#     print(f" Pagina no encontrada")

# else:
#     if (page.status_code == 200):
#         print("Correcto")
#         print(page.content)
#     else:
#         print("Incorrecto")


import requests
from abc import ABC, abstractmethod


class IapiConsultor(ABC):
    @abstractmethod
    def checkConnection(self,url:str):
        pass



class methodGet(IapiConsultor):
    def checkConnection(self,url:str):
        try:
            return requests.get(url)
        except Exception as error:
            return(error)


class methodDelete(IapiConsultor):
    def checkConnection(self,url:str):
        try:
            return requests.get(url)
        except Exception as error:
            return(error)


class methodPost(IapiConsultor):
    def checkConnection(self,url:str):
        try:
            return requests.get(url)
        except Exception as error:
            return(error)
    

class bussines:
    def __init__(self,consultor:IapiConsultor):
        self.consultor = consultor

    