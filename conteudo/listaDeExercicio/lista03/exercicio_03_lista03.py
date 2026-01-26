# 3. Altere o algoritmo anterior para, além da média, contar os alunos que tiraram entre 0 e 5, 0(0 ≤ nota < 5, 0) e acima de 5, 0 (nota ≥ 5, 0).

alunos = 5
notas = [7, 8, 9, 6, 5]
i = 0
somaNotas = 0
notasAbaixode5 = 0
notasACimade5 = 0
media = 0

while i < alunos:
    somaNotas += notas[i]
    if notas[i] < 5.0:
        notasAbaixode5 += 1
    else:
        notasACimade5 += 1
    i += 1

media = somaNotas / alunos

print(f'A média da turma é: {media}'
      f'\nQuantidade de alunos com nota abaixo de 5: {notasAbaixode5}'
      f'\nQuantidade de alunos com nota acima ou igual a 5: {notasACimade5}')