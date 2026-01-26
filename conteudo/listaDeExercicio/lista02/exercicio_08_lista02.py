# 8. No exercício da calculadora, visto em sala de aula, temos um problema com a operação de divisão.
# Sua tarefa será exibir uma mensagem informando que é impossível fazer uma divisão por 0.
# Note que, essa mensagem só deverá aparecer quando o usuário quiser fazer tal operação.

num_a = float(input("Digite o primeiro número: "))
operador = input("Digite a operação (+, -, *, /): ")
num_b = float(input("Digite o segundo número: "))
resultado = 0

match operador:
    case "+":
        resultado = num_a + num_b
    case "-":
        resultado = num_a - num_b
    case "*":
        resultado = num_a * num_b
    case "/":
        if num_b == 0:
            print("Erro: Divisão por zero é impossível.")
        else:
            resultado = num_a / num_b
    case _:
        print("Operação inválida.")

print(f"O resultado é: {resultado}")