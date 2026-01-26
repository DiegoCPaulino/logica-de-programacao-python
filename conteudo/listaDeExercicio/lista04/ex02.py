# 2. Escreva uma função que recebe como parâmetro um inteiro positivo n e retorna uma listapreenchida com n números inteiros aleatórios entre 1 e 1000.
# 1 import random
# 2
# 3 #gerando um numero aleatorio entre 1 e 1000
# 4 numero = random.randint(1,1001)

import random
n = 3

def escolheNumero(n):
    numeros = []
    for i in range(n):
        numero = random.randint(1, 1001)
        numeros.append(numero)
    return numeros

print(escolheNumero(n))