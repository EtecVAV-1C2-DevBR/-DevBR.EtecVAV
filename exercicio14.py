def p(n):
    if n < 1:
        return None
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Digite um número: "))
print("É primo?", eh_primo(n))