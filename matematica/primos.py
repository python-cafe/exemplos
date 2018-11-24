import math


def eh_primo(n):
    # raiz = n**(0.5)
    raiz = int(math.sqrt(n))
    for d in range(2, raiz +1):
        if n % d == 0:
            return False
    return True


numero = int(input("Digite um número: "))
if eh_primo(numero):
    print("O número {} é primo".format(numero))
else:
    print("O número {} NÃO é primo".format(numero))
