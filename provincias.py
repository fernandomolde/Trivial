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
        # Obsoleto
        manejador = Sql(BD)
        campos = 'codigo,descripcion'
        valores = f'{self.__codigo},"{self.__descripcion}"'
        nuevo_id = manejador.insertar(Provincia.tabla,campos,valores)
        return nuevo_id
    
    def actualizar(self):
        #TODO: Poner try
        # Obsoleto
        manejador = Sql(BD)
        campos = 'codigo,descripcion'
        valores = f'{self.__codigo},{self.__descripcion}'
        nuevo_id = manejador.actualizar(Provincia.tabla,campos,valores,self.__id)
        return nuevo_id

    def guardar(self):
        #TODO: Poner try
        manejador = Sql(BD)
        campos = 'codigo,descripcion'
        valores = f'{self.__codigo},{self.__descripcion}'
        if self.__id:
            nuevo_id = manejador.actualizar(Provincia.tabla,campos,valores,self.__id)
            return nuevo_id
        else:
            nuevo_id = manejador.insertar(Provincia.tabla,campos,valores)
            return nuevo_id
       
    def leer_por_id(self):
        """
        
        Buscar en la bd un objeto con el id pasado como parámetro.
        Si existe devuelve un objeto con esas propiedades.
        Si no existe devuelve none

        """
        id_provincia = self.__id
        #TODO: Poner Try
        manejador = Sql(BD)
        lista = manejador.seleccionar(f'select * from T_Provincias where id = {id_provincia}')
        if lista:
            return Provincia(lista[0][1],lista[0][2],lista[0][0])
        else:
            return None

    def borrar(self):
        """
        
        Borra de la bd un objeto con el id pasado como parámetro.
        Si existe devuelve el número de filas borradas (1).
        Si no existe devuelve none

        """
        id_provincia = self.__id
        manejador = Sql(BD)
        resp = manejador.borrar(Provincia.tabla,'id',id_provincia)
        return resp