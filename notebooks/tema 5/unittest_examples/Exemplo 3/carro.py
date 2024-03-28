"""
Baseado no exemplo apresentado em
https://www.jetbrains.com/help/pycharm/testing-your-first-python-application.html#write-test
"""


class Carro:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade
        self.odometro = 0
        self.tempo = 0

    def mostrar_estado(self):
        print(f"=> Vou a {self.velocidade} km/h!")

    def acelerar(self):
        """Acrescentar 5 (km/h) à velocidade; 0 <= velocidade <= 40"""
        self.velocidade = min(self.velocidade + 5, 40)

    def travar(self):
        """Diminuir 5 (km/h) à velocidade; 0 <= velocidade <= 40"""
        self.velocidade = max(self.velocidade - 5, 0)

    def step(self):
        self.odometro += self.velocidade
        self.tempo += 1

    def calcular_velocidade_media(self):
        if self.tempo != 0:
            return self.odometro / self.tempo


if __name__ == "__main__":
    import msvcrt
    from aux_print_with_frame import print_with_frame

    # Inicializar o carro
    carro = Carro()
    print("Vrumm!!")

    while True:
        # Mostrar o menu de ações
        print_with_frame(
            "Sou um carro! O que faço?\n[A]celero, [T]ravo, mostro [O]dometro, ou mostro a [V]elocidade media? ([S]air)"
        )
        # Ler imediatamente a tecla pressionada e converter para maiúsculas
        action = msvcrt.getch().decode("utf-8").upper()
        print(action)

        # Executar a ação
        match action:
            case "A":
                print("Vruuuuuuuum!")
                carro.acelerar()
            case "T":
                print("Ssssskrrrr!")
                carro.travar()
            case "O":
                print(f"Percorri {carro.odometro} kms.")
            case "V":
                print(
                    f"A velocidade media foi de {carro.calcular_velocidade_media():.2f} Km/h."
                )
            case "S":
                print(
                    "Vruu-vruu-vruum... tchss. Desligado. Clic... Creeeak... Thump. Beep-beep!"
                )
                exit(0)
            case _:
                print("Não sei o que fazer!")
                continue

        # Atualizar o estado do carro
        carro.step()
        carro.mostrar_estado()
