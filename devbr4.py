def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("bem vindo ao descobridor de primos: "))

menor_primo = None
maior_primo = None

for i in range(2, n + 1):
    if primo(i):
        if menor_primo is None:
            menor_primo = i
        maior_primo = i

if menor_primo and maior_primo:
    print("Menor primo até", n, "é:", menor_primo)
    print("Maior primo até", n, "é:", maior_primo)
else:
    print("Não há números primos até", n)