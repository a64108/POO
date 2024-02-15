# ========================================================================
# UALG - POO 
# Aluno - 64108
# Exercicio - 4 - A
# ========================================================================

# Faça um programa que leia um vetor de 5 números inteiros e mostre-os.

# Função para ler um vetor de 5 números inteiros
def ler_vet():
    vetor = []
    for tamanho in range(5):
        num = int(input(f"Digite o {tamanho + 1}º número inteiro: "))
        vetor.append(num)
    return vetor

# Função para mostrar os elementos do vetor
def ver_vetor(vetor):
    print("Os números escritos são:")
    for num in vetor:
        print(num, end=" ")

# Chama as funções e exibe o vetor
vet_num = ler_vet()
ver_vetor(vet_num)