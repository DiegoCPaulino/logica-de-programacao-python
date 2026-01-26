# 11. Se Fn é o n-ésimo número da sequência de Fibonacci, podemos calculá-la através da seguinte fórmula de recorrência:
# Vamos mostrar os 10 primeiros números da sequência de Fibonacci:
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# Escreva um algoritmo que dado n, calcula o n-ésimo número da sequência de Fibonacci.

num = int(input("Digite um número inteiro positivopara calcular o n-ésimo número da sequência de Fibonacci: "))
a, b = 1, 1

if num == 1 or num == 2:
    fibonacci_num = 1
else:
    for _ in range(3, num + 1):
        a, b = b, a + b
    fibonacci_n = b

print(f"O {num}-ésimo número da sequência de Fibonacci é: {fibonacci_num}")