# Video Strings e Criptografia
# Solução usando uma lista e convertendo-a em string ao final

chave = 3
mensagem = "Imperdivel"
# tamanho tabela ASCII
n = 128

cifrada = list(mensagem)
i = 0
# você pode usar a string 'mensagem' ou a lista 'cifrada' no FOR
for letra in mensagem:
    # achar no alfabeto a letra que esteja chave posições a frente
    indice = ord(letra)
    # substituir na mensagem a letra pela nova_letra
    cifrada[i] = chr((indice + chave)%n)
    i = i+1

print("Original: ", mensagem)
# converte a lista em string novamente
cifrada = "".join(cifrada)
print("Cifrada:", cifrada)
