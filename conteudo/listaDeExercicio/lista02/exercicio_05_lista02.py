# 5. Faça um programa para ler dois números inteiros A e B e informar se A é divisível por B.

num_a = int(input("Digite o primeiro número inteiro: "))
num_b = int(input("Digite o segundo número inteiro: "))

if num_a % num_b == 0:
    print(f"{num_a} é divisível por {num_b}.")
else:
    print(f"{num_a} não é divisível por {num_b}.")