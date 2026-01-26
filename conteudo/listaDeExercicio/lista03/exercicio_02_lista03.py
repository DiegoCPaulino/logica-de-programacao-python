# 2. Dados o número n de alunos de uma turma de Algoritmos e suas notas da primeira prova, determinar a média das notas dessa turma.
# Considere que o usuário digite as informações corretamente.

alunos = 5
notas = [7, 8, 9, 6, 5]
i = 0
somaNotas = 0
media = 0

while i < alunos:
    somaNotas += notas[i]
    i += 1

media = somaNotas / alunos

print(f'A média da turma é: {media}')