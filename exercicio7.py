#Sequência de valores inteiros

primeira = list(map(int, input("Primeira sequência: ").split()))

segunda = list(map(int, input("Segunda sequência: ").split()))

contagem = 0
n = len(primeira)
m = len(segunda)

for i in range(m - n + 1):
    if segunda[i:i+n] == primeira:
        contagem += 1

print("Resultado:", contagem)
