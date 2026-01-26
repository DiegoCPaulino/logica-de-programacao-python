# 9. Uma equação de 2º grau é da forma: ax2 + bx + c = 0, onde a ̸= 0.
# Escreva um algoritmo que recebe os três coeficientes da equação, calcula e imprime as raízes reais se for possível.
# Use a seguinte fórmula para resolver a equação:

import math

a = float(input("Digite o coeficiente a (a ≠ 0): "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

if a == 0:
    print("O coeficiente 'a' não pode ser zero em uma equação de 2º grau.")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"A equação possui uma raiz real: {raiz}")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"A equação possui duas raízes reais: {raiz1} e {raiz2}")