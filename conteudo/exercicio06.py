salario = float(input("Digite o salário do funcionário: "))
contribuicao = 0

if salario <= 1693.72:
    contribuicao = salario * 0.08
elif salario <= 2822.90:
    contribuicao = salario * 0.09
elif salario <= 5645.80:
    contribuicao = salario * 0.11
else:
    contribuicao = 621.038
print(f"A contribuição do INSS é: R$ {contribuicao:.2f}")