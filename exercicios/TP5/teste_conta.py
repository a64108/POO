"""
UALG - 2023/2024
Disciplina - POO
a64108 - André Vieira
"""

import unittest
from conta import Conta


class TestConta(unittest.TestCase):
    def setUp(self):
        self.conta = Conta("samurai jack", 2, 1000)

    def test_titular(self):
        self.assertEqual(self.conta.titular, "Samurai Jack")

    def test_str(self):
        self.assertEqual(
            self.conta.__str__(),
            "Conta de Samurai Jack, com um saldo de €1000 e taxa de juro a prazo de 10 %",
        )

    def test_taxa_de_juro_prazo(self):
        self.assertIsInstance(self.conta.taxa_de_juro_prazo, (int, float))
        self.assertGreaterEqual(self.conta.taxa_de_juro_prazo, 0)

    def test_saldo(self):
        self.assertIsInstance(self.conta.saldo, (int, float))
        self.assertGreaterEqual(self.conta.saldo, 0)
        self.conta.saldo = -10
        self.assertGreaterEqual(self.conta.saldo, 0)

    def test_capitaliza_juros(self):
        self.conta.capitaliza_juros()
        self.assertAlmostEqual(self.conta.saldo, 1020)

    def test_cobra_comissao_bancaria(self):
        # sucesso a cobrar
        self.conta.saldo = 1000
        valor = 10
        cobrado = self.conta.cobra_comissao_bancaria(valor)
        self.assertAlmostEqual(self.conta.saldo, 990)
        self.assertEqual(cobrado, 10)

        # falha a cobrar
        self.conta.saldo = 100
        valor = 200
        cobrado = self.conta.cobra_comissao_bancaria(valor)
        self.assertAlmostEqual(self.conta.saldo, 0)
        self.assertEqual(100, cobrado)

        # sucesso em levantamento
    def test_faz_levantamento(self):
        self.conta.saldo = 1000
        valor = 100
        resp = self.conta.faz_levantamento(valor)
        self.assertTrue(resp)
        self.assertAlmostEqual(self.conta.saldo, 900)

        # falha em levantamento
        self.conta.saldo = 100
        valor = 200
        resp = self.conta.faz_levantamento(valor)
        self.assertFalse(resp)
        self.assertAlmostEqual(self.conta.saldo, 100)

        # teste de deposito
    def test_faz_deposito(self):
        self.conta.saldo = 1000
        valor = 100
        self.conta.faz_deposito(valor)
        self.assertAlmostEqual(self.conta.saldo, 1100)


if __name__ == "__main__":
    unittest.main()