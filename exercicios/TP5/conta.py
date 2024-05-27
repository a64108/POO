# conta.py

class Conta:
   """Classe que representa uma conta bancária."""

   def __init__(self, titular, taxa_de_juro_prazo=0, saldo=0):
      pass

   def __str__(self):
      pass

   @property
   def titular(self):
      """Devolve o titular da conta."""
      pass

   @titular.setter
   def titular(self, valor):
      """Guarda uma string formatada em "title".
      (e.g., 'luigi vercotti' -> 'Luigi Vercotti)"""
      pass

   @property
   def taxa_de_juro_prazo(self):
      """Devolve a taxa de juro a prazo."""
      pass

   @taxa_de_juro_prazo.setter
   def taxa_de_juro_prazo(self, valor):
      """Guarda a taxa de juro a prazo.
      Deve ser numérica, em percentagem (0-100%).
      A taxa_de_juro não pode ser negativa, sendo que se for fornecido
      um valor negativo a taxa_de_juro é colocada a 0.
      """
      pass

   @property
   def saldo(self):
      """Devolve o saldo"""
      pass

   @saldo.setter
   def saldo(self, valor):
      """Guarda o saldo. Deve ser numérico.
      O saldo não pode ser negativo, sendo que se for fornecido
      um valor negativo o saldo é colocado a 0.
      """
      pass

   def capitaliza_juros(self):
      """Acrescenta os juros ao saldo.
      E.g., se saldo = 1000 e taxa_juro = 2 então saldo passa a 1020
      """
      pass

   def cobra_comissao_bancaria(self, valor):
      """O valor da comissão é retirado ao saldo.
      Se o saldo for maior do que a comissão então cobra tudo, senão
      cobra o equivalente ao existente em saldo.
      E.g.:
      saldo = 10 e comissão = 5 -> saldo = 5 e cobrado = 5
      saldo = 10 e comissão = 15 -> saldo = 0 e cobrado = 10

      :return: valor descontado ao saldo
      """
      pass

   def faz_levantamento(self, valor):
      """
      Subtrai ao saldo o valor desde que o saldo se mantenha positivo.
      :return: True se o levantamento foi possível, False caso contrário.
      """
      pass

   def faz_deposito(self, valor):
      """Acrescenta ao saldo o valor"""
      pass


if __name__ == "__main__":
   conta = Conta("Quim")
   print(conta.titular, conta.taxa_de_juro_prazo, conta.saldo)