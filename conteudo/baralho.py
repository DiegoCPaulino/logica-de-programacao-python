import random

def cria() -> list:
    monte = [[valor, naipe] for valor in range(1, 14) for naipe in ['ouros', 'copas', 'paus', 'espadas']]
    return monte

def embaralha(baralho: list):
    for i in range(0, len(baralho)):
        j = random.randint(0, len(baralho) - 1)
        aux = baralho[i]
        baralho[i] = baralho[j]
        baralho[j] = aux

    return baralho
   
def compra(baralho: list) -> list:
    if len(baralho) > 0:
        return baralho.pop()
    else:
        return None
    
def toString(carta: list) -> str:
    resp = ''
    if carta[0] == 1:
        resp += 'A'
    elif carta[0] == 11:
        resp += 'J'
    elif carta[0] == 12:
        resp += 'Q'
    elif carta[0] == 13:
        resp += 'K'
    else:
        resp += str(carta[0])

    if carta[1] == 'ouros':
        resp += '♦'
    elif carta[1] == 'copas':
        resp += '♥'
    elif carta[1] == 'paus':
        resp += '♣'
    else:
        resp += '♠'

    return resp


if __name__ == '__main__':
    monte = cria()
    embaralha(monte)

    carta = compra(monte)
    while carta != None:
        print(toString(carta))
        carta = compra(monte)