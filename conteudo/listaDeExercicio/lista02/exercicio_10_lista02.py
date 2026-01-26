# 10. Escreva um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de pagamento.
# Utilize os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.
# código condição de pagamento:
# 1 - A vista em dinheiro ou cheque, recebe 10% de desconto
# 2 - A vista no cartão de crédito, recebe 5% de desconto
# 3 - Em duas vezes, preço normal de etiqueta sem juros
# 4 - Em quatro vezes, preço normal de etiqueta mais juros de 7%

preco_etiqueta = float(input("Digite o valor do produto: "))
print("Condições de pagamento:")
print("1 - À vista em dinheiro ou cheque (10% de desconto)")
print("2 - À vista no cartão de crédito (5% de desconto)")
print("3 - Em duas vezes (preço normal de etiqueta)")
print("4 - Em quatro vezes (preço normal de etiqueta mais juros de 7%)")
condicao_pagamento = int(input("Escolha a condição de pagamento (1-4): "))

valor_final = 0

if condicao_pagamento == 1:
    valor_final = preco_etiqueta * 0.90
elif condicao_pagamento == 2:
    valor_final = preco_etiqueta * 0.95
elif condicao_pagamento == 3:
    valor_final = preco_etiqueta
elif condicao_pagamento == 4:
    valor_final = preco_etiqueta * 1.07
else:
    print("Condição de pagamento inválida. Considerando preço normal de etiqueta.")
    valor_final = preco_etiqueta

print(f"O valor final a ser pago é: R$ {valor_final:.2f}")