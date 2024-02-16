# ========================================================================
# UALG - POO 
# Aluno - 64108
# Exercicio - 4 - B
# ========================================================================

# Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

def ler_vet():
    vetor = []
    for tamanho in range(10):
        num = int(input(f"Digite o {tamanho + 1}º número inteiro: "))
        vetor.append(num)
    return vetor

# Função para mostrar os elementos do vetor
def ver_vetor_reverso(vetor):
    print("Os números escritos são:")
    for num in reversed(vetor):
        print(num, end=" ")

# Chama as funções e exibe o vetor
vet_num = ler_vet()
ver_vetor_reverso(vet_num)