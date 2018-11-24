# Resposta ao desafio proposto no vídeo Strings e Criptografia

chave = 3
# mensagem = "AbACaXI"
mensagem = "Em noite de lua cheia, enquanto o Canguçu esturra, o Guatipuru sobe na Carapanaúba?"

# número das letras nas extremidades do alfabeto
nA = ord('A')
nZ = ord('Z')
na = ord('a')
nz = ord('z')

cifrada = ""
for caracter in mensagem:
    # achar no alfabeto a letra que esteja chave posições a frente
    ind = ord(caracter)
    # Se estiver no intervalo de letras maiúsculas
    if nA <= ind <= nZ:
        nova_letra = chr((ind + chave)%(nZ+1) + ((ind + chave)//(nZ+1))*nA)
        # substituir na mensagem a letra pela nova_letra
        cifrada = cifrada + nova_letra
    # Outra forma de verificar se esta no intervalo de letras (agora) minúsculas
    # lembrar que range gera intervalos da forma [a, b), portanto somamos 1
    elif ind in range(na, nz + 1):
        nova_letra = chr((ind + chave)%(nz+1) + ((ind + chave)//(nz+1))*na)
        cifrada = cifrada + nova_letra
    # Se não for letra
    else:
        cifrada = cifrada + caracter


print("Original: ", mensagem)
print("Cifrada: ", cifrada)
