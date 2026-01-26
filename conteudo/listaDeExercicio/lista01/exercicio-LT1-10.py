salario = float(input('Digite o salário do funcionário: '));
novo_salario = float(input('Digite o novo salário do funcionário: '))

percentual_aumento = ((novo_salario - salario) / salario) * 100;

print(f'O percentual de aumento foi de {percentual_aumento} %');