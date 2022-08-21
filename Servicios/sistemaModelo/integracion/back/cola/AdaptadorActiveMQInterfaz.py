
from abc import ABC, abstractmethod

class AdaptadorActiveMQInterfaz(ABC):

    #Pemrite enviar el paquete al back
    @abstractmethod
    def enviarPayload(self, payload):
        pass

    # Permite eliminar la conexión con el back
    @abstractmethod
    def desconectar(self):
        pass