# ========================================================================
# UALG - POO 
# Aluno - 64108
# Exercicio - 2 - C
# ========================================================================

# Faça um programa que verifique se uma letra digitada é «F» ou «M». Conforme a letra escrever: Feminino, Masculino, ou Género Inválido.

# n1 - input - m, f ou a
# n1u - upper

n1 = (input("Qual o seu genero? M ou F?"))
n1u = n1.upper()

if n1u == "M":
    print(f"O genero é masculino.")
elif n1u == "F":
    print(f"O genero é feminino.")
elif n1u == "H":
    print(f"O genero é Helicoptero de Ataque.")

else:
    print("O genero não é válido.")

