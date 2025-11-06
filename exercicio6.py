#Somatório da fatorial

soma = 0  

for i in range(5):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    
    fatorial = 1
    for con in range(1, num + 1):
        fatorial *= con  

    soma += fatorial

print(f"\nA soma dos fatoriais é: {soma}")