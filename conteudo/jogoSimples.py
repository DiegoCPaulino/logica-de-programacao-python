import baralho as bar

deck = bar.cria()
bar.embaralha(deck)

c1 = bar.compra(deck)
c2 = bar.compra(deck)

if c1[0] > c2[0]:
    print(f'Jogador 1 ganhou {bar.toString(c1)} {bar.toString(c2)}')
elif c1[0] < c2[0]:
    print(f'Jogador 2 ganhou {bar.toString(c1)} {bar.toString(c2)}')
else:
    print(f'EMPATE')