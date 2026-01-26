# Escreva um programa que cria uma lista de strings e preenche essa lista com 10 valores que serão digitados pelo usuário. 
# Imprima a lista na tela.

lista = []

def adicionaValor(lista):
    for i in range(10):
        valor = input("Digite um valor: ")
        lista.append(valor)
    return lista

print(adicionaValor(lista))