# lista de multiplicação

lista = [int(x) for x in input("Digite uma sequência de números : ").split()]

C = int(input("Digite o valor de C: "))

encontrado = False

for i in range(len(lista)):
    for j in range(i + 1, len(lista)):  
        if lista[i] * lista[j] == C:
            print(f"Resultado: {lista[i]} e {lista[j]}")
            encontrado = True
            break 
    if encontrado:
        break  

if not encontrado:
    print("Resultado: não existem tais números")
