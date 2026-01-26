# 7. A conversão de graus Fahrenheit para centígrados é obtida pela fórmula C = 5/9 (F − 32).
# Escreva um algoritmo que calcule e escreva uma tabela de graus centígrados em função de graus Fahrenheit que variem de 50 a 150 Fahrenheit de 1 em 1.

print('Fahrenheit  Centígrados')
for fahrenheit in range(50, 151):
    centigrados = (5/9) * (fahrenheit - 32)
    print(f'{fahrenheit}  {centigrados:13.2f}')