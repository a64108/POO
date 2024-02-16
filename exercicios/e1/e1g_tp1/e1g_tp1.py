# ========================================================================
# UALG - POO 
# Aluno - 64108
# Exercicio - 1 - G
# ========================================================================

# Faça um programa que pergunte quanto ganha por hora e o número de horas trabalhadas por mês. Calcule e mostre o total do salário no referido mês.


horas = float(input("Quantas horas trabalhou? "))
pago = float(input("Quando recebe por hora? "))

salario = horas * pago

print(f"Com um salário por hora de {pago}€ e com {horas} trabalhadas tem um salário mensal de {salario}")