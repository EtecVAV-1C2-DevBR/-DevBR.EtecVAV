def m(v):
    if len(v) == 0:
        return 0
    return sum(v) / len(v)

valores = 0
va = [float(x) for x in input("Digite os números separados por espaço: ").split()]
print("Média =", m(valores))