import unittest
from sql import Sql
from settings import BD

class TestSqlite(unittest.TestCase):
    def test_existencia(self):
        mi_bd = Sql(BD)
        cnx = mi_bd.conectar()
        self.assertIsNotNone(cnx)

    def test_seleccionar(self):
        mi_bd = Sql(BD)
        consulta = 'select * from articulos '
        resultado = mi_bd.seleccionar(consulta)
        self.assertIsNotNone(resultado)

    def test_borrado(self):
        mi_bd = Sql(BD)
        resultado = mi_bd.borrar('articulos','id')
        self.assertEqual(resultado,1)
    
    def test_insercion_articulo(self):
        mi_bd = Sql(BD)
        campos = 'codigo, descripcion,precio'
        valores = '"1234","Nada","123"'
        resultado = mi_bd.insertar('articulos',campos,valores)
        self.assertIsNotNone(resultado)
    
    def test_actualizacion(self):
        mi_bd = Sql(BD)
        campos = 'codigo, descripcion,precio'
        valores = '"1234","Nada","123"'
        mi_id = 28
        resultado = mi_bd.actualizar('articulos',campos,valores,mi_id)
        self.assertEqual(resultado,1)