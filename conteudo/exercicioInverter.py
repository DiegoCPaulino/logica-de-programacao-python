numeros = [1,2,3,4,5]

# def inverter_lista(numeros):
#     return list(reversed(numeros))

# print(inverter_lista(numeros))

def inverterLista(lista: list) -> None:
    i = 0
    j = len(lista) - 1
    while i < j:
        varTemp = lista[i]
        lista[i] = lista[j]
        lista[j] = varTemp
        i += 1
        j -= 1