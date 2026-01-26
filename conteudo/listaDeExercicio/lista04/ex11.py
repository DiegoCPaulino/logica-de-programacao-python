# 11. Na Copa do Mundo do Brasil os quadrifinalistas foram, em ordem alfabética:
# Alemanha, Argentina, Bélgica, Brasil, Colômbia, Costa Rica, França e Holanda.
# Imaginando que não sabemos os resultados e nem os cruzamentos, escreva um algoritmo que gere todos os possíveis campeões e vice-campeões dentre os oito selecoes.



import itertools

selecoes = ["Alemanha", "Argentina", "Bélgica", "Brasil", "Colômbia", "Costa Rica", "França", "Holanda"]

def geraCampeoesVice(selecoes):
    qntCombinacoes = 0
    for campeao, vice in itertools.permutations(selecoes, 2):
        print("🥇 Campeão: {}"
        "\n🥈 Vice-campeão: {}"
        "\n------------------------------".format(campeao, vice))
        qntCombinacoes += 1
    print(f'➡️ Número de combinações possíveis: {qntCombinacoes}')

geraCampeoesVice(selecoes)