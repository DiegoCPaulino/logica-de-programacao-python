rm_aluno = input('Digite o número do RM do aluno: ')
digitos = [int(d) for d in rm_aluno]
soma_rm = sum(digitos)

print(f'A soma dos dígitos do RM é: {soma_rm}')