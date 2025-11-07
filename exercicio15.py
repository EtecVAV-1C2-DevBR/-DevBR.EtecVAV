a = int(input("Digite um ano: "))

if (a % 400 == 0) or (a % 4 == 0 and a % 100 != 0):
    print("Ano bissexto")
else:
    print("Ano não bissexto")