# 6. A raiz quadrada é uma operação que apenas aceita números positivos.
# Escreva um algoritmo que lê um número qualquer e retorna a raiz quadrada desse número se possível.
# Use a função math.sqrt(<numero>) para calcular a raiz quadrada em Python.
# Note que, para usar essa função, você terá que importar o módulo math antes.

import math

num = float(input("Digite um número: "))

if num >= 0:
    raiz_quadrada = math.sqrt(num)
    print(f"A raiz quadrada de {num} é {raiz_quadrada:.2f}.")
else:
    print("Não é possível calcular a raiz quadrada de um número negativo.")