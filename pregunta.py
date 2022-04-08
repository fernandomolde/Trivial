import respuesta

class Pregunta():
    def __init__(self,id,cuerpo,tematica='general',dificultad=0) -> None:
        self.__id = id
        self.__cuerpo = cuerpo
        self.__tematica = tematica
        self.__dificultad = dificultad
        self.respuestas = [] # Colección de objetos Respuesta
        
    @property
    def id(self):
        return self.__id

    @property
    def cuerpo(self):
        return self.__cuerpo

    @property
    def tematica(self):
        return self.__tematica

    @property
    def dificultad(self):
        return self.__dificultad
    

        