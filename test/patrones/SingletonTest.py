import unittest

from src.model.dbModel.DBCuas import DBCuas


class SingletonTest(unittest.TestCase):
    def setUp(self):
        self.obj1 = DBCuas()
        self.obj2 = DBCuas()

    def testSonIguales(self):
        self.assertEqual(self.obj1, self.obj2)
        self.assertIs(self.obj1, self.obj2)


if __name__ == '__main__':
    unittest.main()