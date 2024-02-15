# ========================================================================
# UALG - POO 
# Aluno - 64108
# Exercicio - 2 - D
# ========================================================================

# Faça um programa que verifique se uma letra digitada é vogal ou consoante.

# n1 - input - vogal ou consonante
# n1u - upper

n1 = input("Introduza um caracter: ")

if len(n1) == 1:    # verifica se ha um caracter
    n1 = n1.lower() # converte qualquer caracter para lower case

    
    if n1 in "aeiou":
        print("É uma vogal.")
    elif n1.isdigit():
        print("É um número.")
    else:
        print("É uma consoante.")
else:
    print("Please enter only a single character.")