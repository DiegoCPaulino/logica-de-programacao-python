# 3. Escreva um algoritmo que pede para o usuário digitar 10 strings uma de cada vez.
# Depois que o usuário digitar todas elas, seu programa deverá imprimir as strings na ordem inversa de leitura.
# Por exemplo se as duas últimas strings foram, respectivamente, avestruz e onça; o programa imprime onça e depois avestruz.


def definePalavras(palavras):
    for i in range(10):
        palavra = input("Digite a palavra {}: ".format(i + 1))
        palavras.append(palavra)
    return palavras

def imprimePalavrasInvertidas(palavras):
    for palavra in reversed(palavras):
        print(palavra)