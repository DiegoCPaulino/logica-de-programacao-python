# 3. Escreva um algoritmo para ler o nome de 2 times e o número de gols marcados em uma partida.
# Escrever o nome do vencedor. Caso não haja vencedor deverá ser impresso a palavra EMPATE.

time1 = input("Digite o nome do primeiro time: ")
gols_time1 = int(input(f"Digite o número de gols marcados pelo {time1}: "))

time2 = input("Digite o nome do segundo time: ")
gols_time2 = int(input(f"Digite o número de gols marcados pelo {time2}: "))

if gols_time1 > gols_time2:
    print(f"O vencedor é o {time1}!")
elif gols_time2 > gols_time1:
    print(f"O vencedor é o {time2}!")
else:
    print("EMPATE!")