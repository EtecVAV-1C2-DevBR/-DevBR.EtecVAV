tipo = input("Digite 'C' para Celsius ou 'F' para Fahrenheit: ").upper()
temp = float(input("Digite a temperatura: "))

if tipo == 'C':
    f = (temp * 9/5) + 32
    print(f"{temp}°C = {f:.2f}°F")
elif tipo == 'F':
    c = (5/9) * (temp - 32)
    print(f"{temp}°F = {c:.2f}°C")
else:
    print("Unidade inválida. Use apenas 'C' ou 'F'.")