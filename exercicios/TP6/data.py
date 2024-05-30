"""
UALG - 2023/2024
Disciplina - POO
a64108 - André Vieira
"""

class AnoInvalido(Exception):
    """Exceção de ano inválido."""

    def __init__(self, ano):
        super().__init__(f"Ano inválido: {ano}. Não pode ser 0.")


class MesInvalido(Exception):
    """Exceção de mes inválido (1 a 12)."""

    def __init__(self, mes):
        super().__init__(f"Mês inválido: {mes}. Numero do mes tem de ser 1 a 12.")


class DiaInvalido(Exception):
    """Exceção de dia inválido."""

    def __init__(self, dia, mes):
        super().__init__(f"Dia inválido: {dia}, em {mes}.")


class Data:
    """
    Classe da Data em que verifica se a data é valiada ou nao

    Se for invalido levanta um valor de exceçao
    """

    def __init__(self, ano, mes, dia):
        self.validar_data(ano, mes, dia)
        self.ano, self.mes, self.dia = ano, mes, dia

    def __str__(self):
        return f"{self.ano}/{self.mes:02d}/{self.dia:02d}"

    @staticmethod
    def validar_data(ano, mes, dia):
        """
        Levanta exceções para datas inválidas.

        ano - Ano da data.
        mes - Mês da data.
        dia - Dia da data.

        exceçao AnoInvalido: Exceção de ano inválido.
        exceçao MesInvalido: Exceção de mes inválido (1 a 12).
        exceçao DiaInvalido: Exceção de dia inválido.
        """
        if ano < 1:
            raise AnoInvalido(ano)

        if mes <= 0 or mes >= 13:
            raise MesInvalido(mes)

        if 1 > dia > 31:
            raise DiaInvalido(dia, mes)

        if not Data.is_bissexto(ano):
            if dia > 28:
                raise DiaInvalido(dia, mes)
        elif Data.is_bissexto(ano):
            if dia > 29:
                raise DiaInvalido(dia, mes)

        if mes in [4, 7, 9, 11]:
            if dia >= 31:
                raise DiaInvalido(dia, mes)

    @staticmethod
    def is_bissexto(ano):
        """
        Verifica se o ano é bissexto.

        ano - Ano a ser verificado.
        return bool - True se bissexto; False se não.
        """
        return ano % 400 == 0 or ((ano % 4 == 0) and (ano % 100 != 0))