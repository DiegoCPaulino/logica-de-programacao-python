# 12. Desenvolva um algoritmo que informe se uma data é válida ou não.
# O algoritmo deverá ler 2 números inteiros, que representem o dia e o mês e informar se é um dia do mês válido.
# Desconsidere os casos de ano bissexto, ou seja, fevereiro têm 28 dias.

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))

data_valida = False

if mes in [1, 3, 5, 7, 8, 10, 12]:
    if 1 <= dia <= 31:
        data_valida = True
elif mes in [4, 6, 9, 11]:
    if 1 <= dia <= 30:
        data_valida = True
elif mes == 2:
    if 1 <= dia <= 28:
        data_valida = True

if data_valida:
    print(f"A data {dia:02d}/{mes:02d} é válida.")
else:
    print(f"A data {dia:02d}/{mes:02d} é inválida.")