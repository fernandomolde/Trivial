from sql import Sql
from settings import BD

class Provincia():
    tabla = 'T_provincias'
    def __init__(self,codigo,descripcion,id = None) -> None:
        self.__id = id
        self.__codigo = codigo
        self.__descripcion = descripcion

    def insertar(self):
        #TODO: Poner try
        manejador = Sql(BD)
        campos = 'codigo,descripcion'
        valores = f'{self.__codigo},"{self.__descripcion}"'
        nuevo_id = manejador.insertar(Provincia.tabla,campos,valores)
        return nuevo_id