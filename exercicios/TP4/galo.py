"""
Implementation of the Connect 4 game.
"""

from random import randint
from jogo_abs import Jogo


class Connect4(Jogo):
    """
    Concrete class that inherits from the Jogo class and implements Connect 4.
    """

    def inicializa_tabuleiro(self) -> None:
        """
        Initializes the Connect 4 game board.
        """
        self.numero_de_jogadas_realizadas = 0
        self.linhas = 6
        self.colunas = 7
        # Dictionary representing the board
        self.tabuleiro = {(linha, coluna): " " for linha in range(self.linhas) for coluna in range(self.colunas)}

    def mostra_tabuleiro(self) -> None:
        """
        Draws the Connect 4 game board.
        """
        print(29 * "-")
        for linha in range(self.linhas):
            for coluna in range(self.colunas):
                print(f"| {self.tabuleiro[(linha, coluna)]} ", end="")
            print("|\n" + 29 * "-")
        print("  1   2   3   4   5   6   7")

    def _le_coluna_valida(self, msg: str) -> int:
        """
        Helper method to read a valid column position (1 to 7).
        :param msg: message for the user
        :return: valid column position read from user input
        """
        inputs_validos = {"1", "2", "3", "4", "5", "6", "7"}
        while True:
            pos = input(msg)
            if pos in inputs_validos:
                return int(pos) - 1

    def joga_humano(self, jogador: int) -> None:
        """
        Method that requests the human player's move and places it on the Connect 4 board.
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
        Makes a random move for the computer.
        :param jogador: computer player's number
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
        Checks the stopping condition, i.e., if a player has won.
        :return: `True` if the game has ended, `False` otherwise.
        """
        # Check all winning conditions for Connect 4
        # Check horizontal, vertical, and diagonal (both directions)
        for linha in range(self.linhas):
            for coluna in range(self.colunas - 3):
                if self.tabuleiro[(linha, coluna)] == self.tabuleiro[(linha, coluna + 1)] == self.tabuleiro[(linha, coluna + 2)] == self.tabuleiro[(linha, coluna + 3)] != " ":
                    return True

        for linha in range(self.linhas - 3):
            for coluna in range(self.colunas):
                if self.tabuleiro[(linha, coluna)] == self.tabuleiro[(linha + 1, coluna)] == self.tabuleiro[(linha + 2, coluna)] == self.tabuleiro[(linha + 3, coluna)] != " ":
                    return True

        for linha in range(self.linhas - 3):
            for coluna in range(self.colunas - 3):
                if self.tabuleiro[(linha, coluna)] == self.tabuleiro[(linha + 1, coluna + 1)] == self.tabuleiro[(linha + 2, coluna + 2)] == self.tabuleiro[(linha + 3, coluna + 3)] != " ":
                    return True

        for linha in range(self.linhas - 3):
            for coluna in range(3, self.colunas):
                if self.tabuleiro[(linha, coluna)] == self.tabuleiro[(linha + 1, coluna - 1)] == self.tabuleiro[(linha + 2, coluna - 2)] == self.tabuleiro[(linha + 3, coluna - 3)] != " ":
                    return True

        return False

    def ha_jogadas_possiveis(self) -> bool:
        """
        Checks if there are still possible moves or if the game is a draw.
        :return: `True` if there are still possible moves, `False` otherwise.
        """
        return self.numero_de_jogadas_realizadas < self.linhas * self.colunas


if __name__ == "__main__":
    jogo = Connect4()
    jogo.jogar()
