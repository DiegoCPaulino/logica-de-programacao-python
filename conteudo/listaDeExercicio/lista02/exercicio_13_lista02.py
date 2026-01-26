# 13. Agora, vamos acrescentar na verificação de data os casos de ano bissexto, ou seja, o ano que fevereiro tem 29 dias. Um ano é bissexto se:
# a) o ano for divisível por 4
# b) anos múltiplos de 100, não são bissextos
# c) quando o ano for divisível por 400 ele é bissexto
# d) as últimas regras prevalecem sobre as primeiras
# Para exemplificar um pouco essas regras, observe que 1900 não foi bissexto mas 2000 foi.

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

data_valida = False

if mes in [1, 3, 5, 7, 8, 10, 12]:
    if 1 <= dia <= 31:
        data_valida = True
elif mes in [4, 6, 9, 11]:
    if 1 <= dia <= 30:
        data_valida = True
elif mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        if 1 <= dia <= 29:
            data_valida = True
    else:
        if 1 <= dia <= 28:
            data_valida = True
else:
    data_valida = False
    
if data_valida:
    print(f"A data {dia:02d}/{mes:02d}/{ano} é válida.")
else:
    print(f"A data {dia:02d}/{mes:02d}/{ano} é inválida.")