# 11. Faça um algoritmo que leia as médias semestrais obtidas por um aluno na disciplina de Computational Thinking, o número de aulas ministradas e o número de aulas assistidas por este aluno nesta disciplina.
# Calcule e mostre a média final deste aluno e diga se ele foi aprovado ou reprovado ou está de exame.
# Lembrando que a média do primeiro semestre tem peso 4 e a do segundo peso 6, além disso, o aluno tem que ter frequentado mais de 70% das aulas.

media1 = float(input("Digite a média do primeiro semestre: "))
media2 = float(input("Digite a média do segundo semestre: "))

aulas_ministradas = int(input("Digite o número de aulas ministradas: "))
aulas_assistidas = int(input("Digite o número de aulas assistidas: "))

media_final = (media1 * 4 + media2 * 6) / 10
frequencia = (aulas_assistidas / aulas_ministradas) * 100

aprovado = False

if frequencia > 70:
    if media_final >= 7:
        aprovado = True
    elif 5 <= media_final < 7:
        print("Aluno está de exame.")
    else:
        aprovado = False

if aprovado:
    print(f"Aluno APROVADO | Média final {media_final:.2f} e frequência {frequencia:.2f}%.")
else:
    print(f"Aluno REPROVADO | Média final {media_final:.2f} e frequência {frequencia:.2f}%.")