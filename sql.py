import sqlite3

class Sql():
    """
    
    Clase para gestionar el trabajo con la base de datos sqlite.
    - Conectarse a la BD
    - Insertar
    - Actualizar
    - Borrar
    - Seleccionar

    """
    #TODO: Eliminar la bd a piñón 

    def __init__(self,bd) -> None:
        
        """
        
        Inicializa con la clase con la propiedad nombre de la bd
        
        """

        self.__base_datos = bd

    def conectar(self):
        """
        
        Conecta/desconecta el código con la base de datos
        
        """
        cnx = sqlite3.connect(self.__base_datos)
        return cnx
        #cnx.close()

    
    def seleccionar(self,consulta):
        """
        
        Ejecutar la consulta de selección de datos y devuelve el resultado
        
        """
        consulta = "select * from articulo"
        cnx = self.conectar()
        #TODO: Ejecutar de dentro de un try
        cursor = cnx.cursor()
        cursor.execute(consulta)
        salida = cursor.fetchall()
        cnx.close()
        return salida
    
   
    
    def borrar(self,tabla,campo_id,valor_id):
        """
        
        Ejecutar la consulta de selección de datos y devuelve el resultado
        
        """
        consulta = f'delete from {tabla} where {campo_id} = {valor_id};'
        cnx = self.conectar()
        #TODO: Ejecutar de dentro de un try
        cnx.execute(consulta)
        cnx.commit()
        cnx.close()
        
    def insertar(self,tabla,lista_campo,lista_valor):
        """ 
        
        Añade un nuevo registro a la tabla pasada como paŕametro.
        La lista de campos debe tener el mismo número de elementos que la de valores.
        La lista de canois es una cadena de campos separados por comas.

        """

        cnx = self.conectar()
        #TODO: Ejecutar de dentro de un try
        consulta = f'insert into {tabla}({lista_campo}) values({lista_valor});'
        cursor = cnx.cursor()
        cnx.execute(consulta)
        salida = cursor.lastrowid
        cnx.commit()
        cnx.close()

        return salida

    def actualizar(self):
        pass    
