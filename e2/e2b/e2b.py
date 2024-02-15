# ========================================================================
# UALG - POO 
# Aluno - 64108
# Exercicio - 2 - B
# ========================================================================

# Faça um programa que peça um valor e mostre se o valor é positivo ou negativo.

# n1 - input - qualquer valor
# result - output - indica se é positivo ou negativo

n1 = float(input("Escreva o número:"))


if n1 > 0:
    print(f"O número {n1} é positivo.")
elif n1 < 0:
    print(f"O número {n1} é negativo.")
else:
    print("O número é zero.")
