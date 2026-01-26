aulas_semanais = int(input("Digite o número de aulas semanais: "))
valor_hora_aula = float(input("Digite o valor da hora-aula: "))

salario_base = aulas_semanais * 4.5 * valor_hora_aula
hora_atividade = salario_base * 0.05
dsr = (salario_base + hora_atividade) / 6
salario_mensal = salario_base + hora_atividade + dsr

print(f"Salário base: R$ {salario_base:.2f}"
      f"\n• Hora-atividade: R$ {hora_atividade:.2f}"
      f"\n• DSR: R$ {dsr:.2f}"
      f"\n• Salário mensal: R$ {salario_mensal:.2f}")