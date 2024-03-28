"""
Basedo no exemplo apresentado em
https://www.jetbrains.com/help/pycharm/testing-your-first-python-application.html#write-test
"""

# Importar o módulo unittest para poder usar a classe TestCase
from unittest import TestCase

# Importar a classe Carro para poder instanciar objetos da classe Carro
from carro import Carro


# Criar uma classe de teste que herda da classe TestCase
class TestCarro(TestCase):
    # O método setUp() é sempre executado antes de cada teste
    def setUp(self):
        self.carro = Carro()


class TestInicio(TestCarro):
    def test_velocidade_inicial(self):
        self.assertEqual(self.carro.velocidade, 0)

    def test_odometro_inicial(self):
        self.assertEqual(self.carro.odometro, 0)

    def test_tempo_inicial(self):
        self.assertEqual(self.carro.tempo, 0)


class TestAcelerar(TestCarro):
    def test_acelerar_desde_zero(self):
        self.carro.acelerar()
        self.assertEqual(self.carro.velocidade, 5)

    def test_acelerar_multiplas_vezes(self):
        for _ in range(3):
            self.carro.acelerar()
        self.assertEqual(self.carro.velocidade, 15)


class TestTravar(TestCarro):
    def test_travar_1_vez(self):
        self.carro.acelerar()
        self.carro.travar()
        self.assertEqual(self.carro.velocidade, 0)

    def test_travar_multiplas_vezes(self):
        for _ in range(5):
            self.carro.acelerar()
        for _ in range(3):
            self.carro.travar()
        self.assertEqual(self.carro.velocidade, 10)

    def test_velocidade_nao_pode_ser_negativa(self):
        self.assertGreaterEqual(self.carro.velocidade, 0)
        self.carro.travar()
        self.assertGreaterEqual(self.carro.velocidade, 0)

    def test_velocidade_nao_passa_dos_40(self):
        for _ in range(10):
            self.carro.acelerar()
        self.assertLessEqual(self.carro.velocidade, 40)

    def test_travar_multiplas_vezes_a_zero(self):
        for _ in range(3):
            self.carro.travar()
        self.assertGreaterEqual(self.carro.velocidade, 0)


# Opcional
if __name__ == "__main__":
    import unittest

    unittest.main(verbosity=2)
