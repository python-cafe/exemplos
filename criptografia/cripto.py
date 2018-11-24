# Video Strings e Criptografia

# abacaxi
#
# a - d
# b - e
# c - f
# x - a
# i - l
#
# dedfdal

alfabeto = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

chave = 3
mensagem = "AbACaXI"
# linha abaixo converte as letras para minúsculas
# mensagem = mensagem.lower()

# tamanho da lista alfabeto
# n = len(alfabeto)
# tamanho tabela ASCII
n = 128

cifrada = ""
for letra in mensagem:
    # achar no alfabeto a letra que esteja chave posições a frente
    # indice = alfabeto.index(letra)
    indice = ord(letra)
    # nova_letra = alfabeto[(indice + chave)%n]
    nova_letra = chr((indice + chave)%n)
    # substituir na mensagem a letra pela nova_letra
    cifrada = cifrada + nova_letra

print("Original: ", mensagem)
print("Cifrada: ", cifrada)
