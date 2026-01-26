# 7. Escreva um algoritmo que recebe a idade de um nadador e mostra sua categoria conforme a tabela a seguir:
# Categoria       Idade
# Infantil        5 a 7
# Juvenil         8 a 10
# Adolescente     11 a 15
# Adulto          16 a 30
# Senior acima de 30

idade = int(input("Digite a idade do nadador: "))

if 5 <= idade <= 7:
    print("Categoria: Infantil")
elif 8 <= idade <= 10:
    print("Categoria: Juvenil")
elif 11 <= idade <= 15:
    print("Categoria: Adolescente")
elif 16 <= idade <= 30:
    print("Categoria: Adulto")
elif idade > 30:
    print("Categoria: Senior")
else:
    print("Idade inválida para categoria de nadador.")