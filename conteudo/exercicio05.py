num_a = float(input("Digite o primeiro número: "))
operador = input("Digite a operação (+, -, *, /): ")
num_b = float(input("Digite o segundo número: "))
resultado = 0

if operador == "+":
    resultado = num_a + num_b
elif operador == "-":
    resultado = num_a - num_b
elif operador == "*":
    resultado = num_a * num_b
elif operador == "/":
    if num_b != 0:
        resultado = num_a / num_b
    else:
        resultado = "Erro: Divisão por zero não é permitida."
else:
    print("Erro: Operação inválida.")
    quit()

print(f"O resultado é: {resultado}")