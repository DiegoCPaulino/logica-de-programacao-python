# 4. Dados n um inteiro positivo e uma sequência de n números reais, escreva um algoritmo que conta e imprime a quantidade de números positivos e a quantidade de números negativos.

numeros = [7, -8, 9, -6, 5, -3, 0]
i = 0
tamanho = len(numeros)
quantidadePositivos = 0
quantidadeNegativos = 0

while i < tamanho:
    if numeros[i] > 0:
        quantidadePositivos += 1
    elif numeros[i] < 0:
        quantidadeNegativos += 1
    i += 1

print(f'Quantidade de números positivos: {quantidadePositivos}'
      f'\nQuantidade de números negativos: {quantidadeNegativos}')