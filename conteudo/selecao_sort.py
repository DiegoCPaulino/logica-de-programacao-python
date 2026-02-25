def menor(lista: list, pos: int) -> int:
    pos_menor = pos
    while pos < len(lista):
        if lista[pos_menor] > lista[pos]:
            pos_menor = pos
        pos += 1
    return pos_menor
def ordena(lista: list):
    for i in range(len(lista) - 1):
        p = menor(lista, i)
        aux = lista[p]
        lista[p] = lista[i]
        lista[i] = aux

# conjunto = [3, 7, -2, 4, 0, 1, -8]

# ordena(conjunto)
# print(conjunto)

lista = [1, 2, 4, 5]

# def addLista(lista: list, valor: int):
#     lista.append(valor)
#     ordena(lista)

# addLista(lista, 3)
# print(lista)

def addLista(lista: list, valor: int):
    lista.append(valor)
    i = len(lista) - 1
    while i >= 0 and lista[i] < lista[i - 1]:
        aux = lista[i]
        lista[i] = lista[i - 1]
        lista[i - 1] = aux
        i -= 1

addLista(lista, 3)
print(lista)