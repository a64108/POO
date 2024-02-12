# ========================================================================
# UALG - POO 
# Aluno - 64108
# Exercicio - 1 - H
# ========================================================================

# Faça um programa que peça a temperatura em graus Fahrenheit, converta-a e mostre-a em graus Celsius: C = 5 × (F – 32)/9.

# tempf - temperatura em fahrenheit, input
# tempc - temepratura em celsius, output

import math

tempf = float(input("Escreva temperatura em Fahrenheit "))

tempc = (tempf - 32) * 5 / 9

print(f"A temperatura {tempf} Fahrenheit é equivalente a {tempc} graus Celsius")