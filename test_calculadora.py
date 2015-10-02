import unittest
from Calculadora import Calculadora


class Test(unittest.TestCase):

    # setup, es el primer metodo que se ejecuta
    # tearDown, es el ultimo metodo que se ejecuta
    def setUp(self):
        self.calc = Calculadora()

    def test_suma_de_2_mas_2(self):
        resultado = self.calc.suma(2, 2)
        self.assertEqual(4, resultado)

    def test_suma_de_3_mas_3(self):
        resultado = self.calc.suma(3, 3)
        self.assertEqual(6, resultado)

    def test_suma_de_5_mas_5(self):
        resultado = self.calc.suma(5, 5)
        self.assertEqual(10, resultado)

    def test_resta_4_menos_3(self):
        resultado = self.calc.resta(4, 3)
        self.assertEqual(1, resultado)

    def test_resta_8_menos_4(self):
        resultado = self.calc.resta(8, 4)
        self.assertEqual(4, resultado)


if __name__ == '__main__':
    unittest.main()
