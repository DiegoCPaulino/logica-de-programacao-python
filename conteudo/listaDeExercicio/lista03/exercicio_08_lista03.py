# 8. Um número inteiro positivo n é denominado primo se existirem apenas dois divisores inteiros positivos dele: o 1 e o próprio n.
# Escreva um algoritmo que recebe um inteiro n e verifica se n é primo ou não.

num = int(input("Digite um número inteiro positivo: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} não é um número primo.")
            break
    else:
        print(f"{num} é um número primo.")