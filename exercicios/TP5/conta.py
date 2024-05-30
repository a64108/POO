"""
UALG - 2023/2024
Disciplina - POO
a64108 - André Vieira
"""

class Conta:
    """Classe das contas."""

    def __init__(self, titular, taxa_de_juro_prazo=0, saldo=0):
        self._titular = titular.title()
        self._taxa_de_juro_prazo = taxa_de_juro_prazo
        self._saldo = saldo

    def __str__(self):
        return f"Conta de {self._titular}, com um saldo de €{self._saldo} e taxa de juro a prazo de {self._taxa_de_juro_prazo} %"

    @property
    def titular(self):
        """Getter do titular da conta."""
        return self._titular

    @titular.setter
    def titular(self, valor):
        """Setter de string formatada para "title".
        (exemplo elvis presley -> Elvis Presley)"""
        self._titular = valor.title()

    @property
    def taxa_de_juro_prazo(self):
        """Getter da taxa de juro a prazo."""
        return self._taxa_de_juro_prazo

    @taxa_de_juro_prazo.setter
    def taxa_de_juro_prazo(self, valor):
        """Setter da taxa de juro a prazo.
        Valor de 0 a 100 (é mais tarde dividido por 100 para fazer o calculo de uma percentagem).
        Caso um numero > 0 for colocado o programa mete o valor a 0.
        """
        if valor < 0:
            self._taxa_de_juro_prazo = 0
        else:
            self._taxa_de_juro_prazo = valor

    @property
    def saldo(self):
        """Devolve o saldo"""
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        """Guarda o saldo. Deve ser numérico.
        O saldo não pode ser negativo, sendo que se for fornecido
        um valor negativo o saldo é colocado a 0.
        """
        if valor < 0:
            self._saldo = 0
        else:
            self._saldo = valor

    def capitaliza_juros(self):
        """Calcula os juros para o saldo.
        Exemplo: Saldo = 1000 e taxa_juro = 10 então saldo = 1100
        """
        juros = self._saldo * self._taxa_de_juro_prazo / 100
        self._saldo += juros

    def cobra_comissao_bancaria(self, valor):
        """saldo = comissao - saldo
        Se:
        saldo = 100 e comissão = 50 -> saldo = 50 e cobrado = 50
        saldo = 100 e comissão = 200 -> saldo = 0 e cobrado = 100
        """
        if self._saldo >= valor:
            self._saldo -= valor
            return valor
        else:
            cobrado = self._saldo
            self._saldo = 0
            return cobrado

    def faz_levantamento(self, valor):
        """
        saldo = saldo - levantamento.
        Se:
        saldo = 100 e levantamento = 50 -> saldo = 50 e levantamento = 50 -> true
        saldo = 100 e levantamento = 200 -> saldo = 50 e levantamento = 0 -> false
        """
        if self._saldo >= valor:
            self._saldo -= valor
            return True
        else:
            return False

    def faz_deposito(self, valor):
        """saldo = saldo + valor"""
        self._saldo += valor


if __name__ == "__main__":
    conta = Conta("Joca")
    print(conta.titular, conta.taxa_de_juro_prazo, conta.saldo)