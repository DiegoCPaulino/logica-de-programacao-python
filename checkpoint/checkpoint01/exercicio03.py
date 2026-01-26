media_ano_anterior = float(input("Digite a média de consumo do ano anterior: "))
consumo_mes_vigente = float(input("Digite o consumo do mês vigente: "))

if consumo_mes_vigente <= 20:
    valor_consumo = consumo_mes_vigente * 2.00
elif consumo_mes_vigente <= 35:
    valor_consumo = consumo_mes_vigente * 3.50
elif consumo_mes_vigente <= 50:
    valor_consumo = consumo_mes_vigente * 5.50
else:
    valor_consumo = consumo_mes_vigente * 7.00

if consumo_mes_vigente < media_ano_anterior:
    desconto = valor_consumo * 0.20
    total_conta = valor_consumo - desconto
    print("** Parabéns! Você economizou água e ganhou um desconto! **"
          f"\n• Valor do consumo: R$ {valor_consumo:.2f}"
          f"\n• Desconto: R$ {desconto:.2f}"
          f"\n• Total da conta: R$ {total_conta:.2f}")
elif consumo_mes_vigente > media_ano_anterior * 1.10:
    multa = valor_consumo * 0.30
    total_conta = valor_consumo + multa
    print("** Atenção! Você excedeu o consumo de água e foi multado! **"
          f"\n• Valor do consumo: R$ {valor_consumo:.2f}"
          f"\n• Multa: R$ {multa:.2f}"
          f"\n• Total da conta: R$ {total_conta:.2f}")
else:
    print("** Seu consumo está dentro da média. **"
          f"\n• Valor do consumo: R$ {valor_consumo:.2f}"
          f"\n• Total da conta: R$ {valor_consumo:.2f}")