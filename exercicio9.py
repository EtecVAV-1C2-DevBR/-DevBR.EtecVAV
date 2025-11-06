# Lista de números inteiros

seq1 = input("Escreva a primeira sequência de números inteiros: ").split()
seq2 = input("Escreva a segunda sequência de números inteiros: ").split()

seq1 = [int(x) for x in seq1]
seq2 = [int(x) for x in seq2]

i, j = 0, 0
resultado = []

while i < len(seq1) and j < len(seq2):
    if seq1[i] <= seq2[j]:
        resultado.append(seq1[i])
        i += 1
    else:
        resultado.append(seq2[j])
        j += 1

resultado.extend(seq1[i:])
resultado.extend(seq2[j:])

print("Resultado:", ' '.join(str(num) for num in resultado))
