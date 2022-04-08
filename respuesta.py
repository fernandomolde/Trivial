class Respuesta():
    def __init__(self,id,cuerpo,conecta=False) -> None:
        self.__id = id
        self.__cuerpo = cuerpo
        self.__conecta = conecta

    @property
    def id(self):
        return self.__id

    @property
    def cuerpo(self):
        return self.__cuerpo

    @property
    def conecta(self):
        return self.__conecta