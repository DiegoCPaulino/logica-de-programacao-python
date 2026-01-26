# 4. A jornada de trabalho diária de um trabalhador é de 8 horas.
# Caso o trabalhador tenha trabalhado além da jornada mensal exigida, ele terá direito a receber hora-extra.
# O valor da hora-extra é o valor que ele recebe por hora acrescido de 50%.
# Supondo que ele trabalhe apenas nos dias úteis, escreva um algoritmo que recebe:
# a) o total de dias úteis de um mês
# b) o total de horas trabalhadas pelo trabalhador
# c) quanto o trabalhador recebe por hora
# Calcula e mostra o valor recebido a título de hora-extra (se houver) e o salário final do trabalhador.

dias_uteis = int(input("Digite o total de dias úteis no mês: "))
horas_trabalhadas = int(input("Digite o total de horas trabalhadas no mês: "))
valor_hora = float(input("Digite quanto o trabalhador recebe por hora: "))

jornada_mensal = dias_uteis * 8
salario_base = horas_trabalhadas * valor_hora
hora_extra = 0


if horas_trabalhadas > jornada_mensal:
    horas_extras_trabalhadas = horas_trabalhadas - jornada_mensal
    valor_hora_extra = valor_hora * 1.5
    hora_extra = horas_extras_trabalhadas * valor_hora_extra
    salario_final = salario_base + hora_extra

print("\n--- Resumo do Salário ---")
print(f"Total de dias úteis no mês: {dias_uteis}")
print(f"Total de horas trabalhadas no mês: {horas_trabalhadas}")
print(f"Valor recebido por hora: R$ {valor_hora:.2f}")
print(f"Salário base: R$ {salario_base:.2f}")
if hora_extra > 0:
    print(f"Valor recebido de hora-extra: R$ {hora_extra:.2f}")
print(f"Salário final do trabalhador: R$ {salario_final:.2f}")