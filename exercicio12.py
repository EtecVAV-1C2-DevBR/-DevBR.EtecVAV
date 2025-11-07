def s(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

n = int(input("Digite um número: "))
print("Soma de 0 até", n, "=", s(n))