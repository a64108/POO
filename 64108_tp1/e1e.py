# ========================================================================
# UALG - POO 
# Aluno - 64108
# Exercicio - 1 - E
# ========================================================================

import math

def calc_area_circ(raio):
    carea = math.pi * raio**2
    return carea

# Example usage:
raio = float(input("Escrever raio do circulo: "))
area_circ = calc_area_circ(raio)

print(f"O raio do circulo é {raio} e a área é {area_circ}")
