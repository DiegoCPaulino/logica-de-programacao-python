# 1. Dada uma sequência de números inteiros onde o último elemento é o 0, escreva um algoritmo 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
i = 0
totalPar = 0
totalImpar = 0

while nums[i] != 0:
    if nums[i] % 2 == 0:
        totalPar += nums[i]
    else:
        totalImpar += nums[i]
    i += 1

print(f'A soma dos números pares é: {totalPar}'
      f'\nA soma dos números ímpares é: {totalImpar}')