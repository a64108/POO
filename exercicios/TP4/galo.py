"""
UALG - 2023/2024
Disciplina - POO
a64108 - André Vieira
"""

from random import randint
from jogo_abs import Jogo


class Connect4(Jogo):
    """
    Classe dentro da classe abstrata jogo
    """

    def inicializa_tabuleiro(self) -> None:
        """
        Inicia o tabuleiro
        """
        self.numero_de_jogadas_realizadas = 0
        self.linhas = 6
        self.colunas = 7
        # Tamanho do tabuleiro
        self.tabuleiro = {(linha, coluna): " " for linha in range(self.linhas) for coluna in range(self.colunas)}

    def mostra_tabuleiro(self) -> None:
        """
        Desenha o tabuleiro no ecra
        """
        print(29 * "-")
        for linha in range(self.linhas):
            for coluna in range(self.colunas):
                print(f"| {self.tabuleiro[(linha, coluna)]} ", end="")
            print("|\n" + 29 * "-")
        print("  1   2   3   4   5   6   7")

    def _le_coluna_valida(self, msg: str) -> int:
        """
        Validação de entradas 1 - 7 depois traduzida de 0 a 6 devido a como python faz os dicionarios
        :param msg: pede ao user por um numero
        :return: caso dentro dos parametros retorna valor
        """
        inputs_validos = {"1", "2", "3", "4", "5", "6", "7"}
        while True:
            pos = input(msg)
            if pos in inputs_validos:
                return int(pos) - 1

    def joga_humano(self, jogador: int) -> None:
        """
        Metodo que chama pelo metodo acima e depois coloca a peça ou pede outro numero que seja valido.
        :param jogador: human player's number
        """
        print(f"\nJogador {jogador}, insira a sua jogada")
        while True:
            coluna = self._le_coluna_valida("Coluna? ")
            for linha in range(self.linhas - 1, -1, -1):
                if self.tabuleiro[(linha, coluna)] == " ":
                    self.tabuleiro[(linha, coluna)] = ["O", "X"][jogador]
                    self.numero_de_jogadas_realizadas += 1
                    return
            print("Coluna cheia. Tente outra coluna!")

    def joga_computador(self, jogador: int) -> None:
        """
        Movimento random do pc
        """
        print("\nÉ a vez do computador jogar...")
        while True:
            coluna = randint(0, self.colunas - 1)
            for linha in range(self.linhas - 1, -1, -1):
                if self.tabuleiro[(linha, coluna)] == " ":
                    self.tabuleiro[(linha, coluna)] = ["O", "X"][jogador]
                    self.numero_de_jogadas_realizadas += 1
                    return

    def terminou(self) -> bool:
        """
        Verifica se o jogo acabou
        :return: true se jogo acabou (player ou pc ganhou) e false se ninguem ganhou ainda
        """
        # Check horizontal
        for linha in range(self.linhas):
            for coluna in range(self.colunas - 3):
                if self.tabuleiro[(linha, coluna)] == self.tabuleiro[(linha, coluna + 1)] == self.tabuleiro[(linha, coluna + 2)] == self.tabuleiro[(linha, coluna + 3)] != " ":
                    return True

        # Check vertical
        for linha in range(self.linhas - 3):
            for coluna in range(self.colunas):
                if self.tabuleiro[(linha, coluna)] == self.tabuleiro[(linha + 1, coluna)] == self.tabuleiro[(linha + 2, coluna)] == self.tabuleiro[(linha + 3, coluna)] != " ":
                    return True

        # Check esquerda para direita a subir
        for linha in range(self.linhas - 3):
            for coluna in range(self.colunas - 3):
                if self.tabuleiro[(linha, coluna)] == self.tabuleiro[(linha + 1, coluna + 1)] == self.tabuleiro[(linha + 2, coluna + 2)] == self.tabuleiro[(linha + 3, coluna + 3)] != " ":
                    return True

        # Check esquerda para a direita a descer
        for linha in range(self.linhas - 3):
            for coluna in range(3, self.colunas):
                if self.tabuleiro[(linha, coluna)] == self.tabuleiro[(linha + 1, coluna - 1)] == self.tabuleiro[(linha + 2, coluna - 2)] == self.tabuleiro[(linha + 3, coluna - 3)] != " ":
                    return True

        return False

    def ha_jogadas_possiveis(self) -> bool:
        """
        contador numero_de_jogadas_realizadas tem de ser menor que n linhas * n colunas senao jogo acaba porque o tabuleiro esta cheio
        """
        return self.numero_de_jogadas_realizadas < self.linhas * self.colunas


if __name__ == "__main__":
    jogo = Connect4()
    jogo.jogar()
