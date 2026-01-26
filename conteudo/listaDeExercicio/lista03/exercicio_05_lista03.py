# 5. Escreva um algoritmo que, dados um número inteiro positivo n, imprime na tela a contagem de todos os divisores positivos de n.

n = int(input('Digite um número inteiro positivo: '))
i = 1
divisores = []

while i <= n:
    if n % i == 0:
        divisores.append(i)
    i += 1

print(f'Os divisores positivos de {n} são: {divisores}')