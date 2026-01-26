# 9. Dados um montante em dinheiro inicial d, uma taxa de juros mensal j e um período de tempo em meses t, escreva um algoritmo que calcula o valor final em dinheiro se d ficar aplicado a taxa de juros j durante t meses.

d = float(input("Digite o montante inicial (d): "))
j = float(input("Digite a taxa de juros mensal (j) em porcentagem: ")) / 100
t = int(input("Digite o período de tempo em meses (t): "))

valor_final = d * (1 + j) ** t

print(f'O valor final após {t} meses é: R$ {valor_final:.2f}')