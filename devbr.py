num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")

if operador == '+':
    print("Resultado:", num1 + num2)
elif operador == '-':
    print("Resultado:", num1 - num2)
elif operador == '*':
    print("Resultado:", num1 * num2)
elif operador == '/':
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Erro: divisão por zero!")
else:
    print("Operador inválido!")