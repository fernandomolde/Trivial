import unittest
from provincias import Provincia

class TestProvincia(unittest.TestCase):
    def test_existencia(self):
        p = Provincia('','')
        self.assertIsNotNone(p)
    
    def test_insert_provincias(self):
        p = Provincia(111,'primera')
        resp = p.insertar()
        self.assertIsNotNone(resp)
