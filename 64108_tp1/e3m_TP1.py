# ========================================================================
# UALG - POO 
# Aluno - 64108
# Exercicio - 3 - M
# ========================================================================

# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo utilizador. Exemplo: 5! = 5 × 4 × 3 × 2 × 1 = 120

# n1 - input - numeero introduzido por user

n1 = float(input("Introduza um numero: "))

def fatorial(n1):
    if n1 == 0 or n1 == 1:
        return 1
    else:
        return n1 * fatorial(n1 - 1)
    



resultado = fatorial(n1)
print(f"O fatorial de {n1} é: {resultado}")