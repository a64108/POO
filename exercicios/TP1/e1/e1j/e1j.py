# ========================================================================
# UALG - POO 
# Aluno - 64108
# Exercicio - 1 - J
# ========================================================================

# Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam 80 euros.
# Informe ao utilizador as quantidades de latas de tinta a serem compradas e o preço total.

# area - input - tamanho da area pintada em m^2
# q_latas - output - quantas latas usou
# preço - output - multiplicar pelo numero de latas

# 1l de tinta para 3m^2
# 1 lata = 18l
# 1 lata = 80€

import math

area = float(input("Escreva a área em metros quadrados "))

q_latas = ((area/3)/18)
q_latas = math.ceil(q_latas)
preco = q_latas*80

print(f"Numa área de {area}m^2s foram utilizadas {q_latas} latas e custou {preco}€")