# ========================================================================
# UALG - POO 
# Aluno - 64108
# Exercicio - 4 - H
# ========================================================================


# Considere o seguinte vetor v= list(range(50))
# Sem utilizar ciclos (i.e. usar slicing), imprima:
# Os primeiros 10 elementos
# Os últimos 10 elementos
# Os valores entre a posição 10 e 20 (inclusive)
# Apague o número na 5.ª posição
# Apague o número 20
# Imprima os números por ordem inversa
# Faça a união com o conjunto ['a', 'b', 'c'] - FALTA FAZER


texto = v= list(range(50))

del texto[5]
texto.remove (20)


print(" Os primeiros 10 caracteres:",texto[:10])
print(" Os ultimos 10 caracteres: ",texto[40:])
print(" Os caracteres entre 10 e 20 (inclusive):",texto[10:21])
print("Lista em ordem reversa:", texto[::-1])


conjunto = ["a","b","c"]
uniao = texto + conjunto
print("União com ['a','b'','c']:", uniao)

