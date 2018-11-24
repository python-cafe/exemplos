import random


def validar_sorteio(participantes, embaralhados):
    for i in range(len(participantes)):
        if participantes[i] == embaralhados[i]:
            return False
    return True

n = int(input("Digite o número de participantes: "))
participantes = []

for i in range(n):
    nome = input("Digite o nome do {}° participante: ".format(i+1))
    participantes.append(nome)


embaralhados = random.sample(participantes, len(participantes))
while not validar_sorteio(participantes, embaralhados):
    embaralhados = random.sample(participantes, len(participantes))

# print("Resultado do Amigo oculto: ")
# for i in range(len(participantes)):
#     print("{} tirou {}".format(participantes[i], embaralhados[i]))

for i in range(len(participantes)):
    arquivo = open("{}.txt".format(participantes[i]), "w")
    arquivo.write(embaralhados[i])
    arquivo.close()
