# 2. Escrever um algoritmo que leia dois valores inteiro distintos e informe qual é o maior ou se houve um empate.

num_a = int(input("Digite o primeiro número inteiro: "))
num_b = int(input("Digite o segundo número inteiro: "))

if num_a > num_b:
    print(f"O maior número é: {num_a}")
elif num_b > num_a:
    print(f"O maior número é: {num_b}")
else:
    print("Houve um empate, os números são iguais.")