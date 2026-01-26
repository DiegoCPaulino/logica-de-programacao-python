# 12. Dizemos que um número natural n é palíndromo se o 1º algarismo de n é igual ao seu último algarismo, o 2º algarismo de n é igual ao penúltimo algarismo, e assim sucessivamente.
# Exemplos: 567765 e 32423 são palíndromos. 567675 não é palíndromo.

num = input("Digite um número inteiro positivo: ")

if num == num[::-1]:
    print(f"{num} é um número palíndromo.")
else:
    print(f"{num} não é um número palíndromo.")