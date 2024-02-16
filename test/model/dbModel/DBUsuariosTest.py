import unittest

from src.model.Usuario import Usuario
from src.model.dbModel.DBUsuarios import DBUsuarios

class DBUsuariosTest(unittest.TestCase):
    def setUp(self):
        self.obj = DBUsuarios()

    def testValidUserAndPass(self):
        self.assertFalse(self.obj.validUserAndPass(1, 2))
        self.assertFalse(self.obj.validUserAndPass(2, None))
        self.assertFalse(self.obj.validUserAndPass(None, 2))
        self.assertFalse(self.obj.validUserAndPass(' ', None))
        self.assertFalse(self.obj.validUserAndPass(None, ' '))
        self.assertFalse(self.obj.validUserAndPass(' ', ' '))
        self.assertFalse(self.obj.validUserAndPass(None, None))
        self.assertIsNotNone(self.obj.validUserAndPass('usertest', '1234'))
        self.assertEqual(self.obj.validUserAndPass('diego', '0000'), 1)

    def testExisteusuario(self):
        self.assertFalse(self.obj.existeUsuario(' '))
        self.assertFalse(self.obj.existeUsuario(None))
        self.assertFalse(self.obj.existeUsuario(1))
        self.assertFalse(self.obj.existeUsuario('usertest1'))
        self.assertTrue(self.obj.existeUsuario('diego'))

    def testGetUsuarioById(self):
        self.assertFalse(self.obj.getUsuarioById(' '))
        self.assertFalse(self.obj.getUsuarioById(None))
        self.assertFalse(self.obj.getUsuarioById(-1))
        self.assertIsInstance(self.obj.getUsuarioById(1), Usuario)

    def testAgregarUsuario(self):
        self.assertFalse(self.obj.agregarUsuario(' ', ' ', ' '))
        self.assertFalse(self.obj.agregarUsuario(None, None, None))
        self.assertFalse(self.obj.agregarUsuario('usertest2', '01234', None))
        self.assertFalse(self.obj.agregarUsuario('usertest3', '1111', '1'))

if __name__ == '__main__':
    unittest.main()