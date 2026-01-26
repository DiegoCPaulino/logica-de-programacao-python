# 10. Escreva um algoritmo que recebe um inteiro positivo n e calcula n! = 1 · 2 · 3 . . . ·(n − 1)· n.
# Por exemplo, se n = 6, então 6! = 1 · 2 · 3 · 4 · 5 · 6 = 720.

num = int(input("Digite um número inteiro positivo: "))
fatorial = 1

for i in range(1, num + 1):
    fatorial *= i

print(f"O fatorial de {num} é: {fatorial}")