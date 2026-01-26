# 6. Em uma prova de concurso com 70 questões haviam 20 pessoas concorrendo.
# Sabendo que cada questão vale 1 ponto, escreva um algoritmo que lê a pontuação da prova obtida de cada um dos candidatos e calcula:
# a) a maior e a menor nota
# b) o percentual de candidatos que acertaram até 20 questões, o percentual que acertaram de 21 a 50 e o percentual que acertou acima de 50 questões

candidatos = 20
notas = [15, 22, 35, 50, 70, 18, 25, 40, 55, 60, 10, 30, 45, 65, 70, 5, 20, 33, 48, 52]
maior_nota = max(notas)
menor_nota = min(notas)

ate_20 = len([nota for nota in notas if nota <= 20])
de_21_a_50 = len([nota for nota in notas if 21 <= nota <= 50])
acima_de_50 = len([nota for nota in notas if nota > 50])

percentual_ate_20 = (ate_20 / candidatos) * 100
percentual_de_21_a_50 = (de_21_a_50 / candidatos) * 100
percentual_acima_de_50 = (acima_de_50 / candidatos) * 100

print(f'Maior nota: {maior_nota}'
      f'\nMenor nota: {menor_nota}'
      f'\nPercentual de candidatos que acertaram até 20 questões: {percentual_ate_20:.2f}%'
      f'\nPercentual de candidatos que acertaram de 21 a 50 questões: {percentual_de_21_a_50:.2f}%'
      f'\nPercentual de candidatos que acertaram acima de 50 questões: {percentual_acima_de_50:.2f}%')