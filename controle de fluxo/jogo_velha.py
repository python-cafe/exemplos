
# tabuleiro = ["X", "O", "X",
#              ["O", "X", "O"],
#              ["0", " ", "X"]]
tabuleiro = [0, 1, 2,
	         3, 4, 5,
	         6, 7, 8]

# horizontal
if tabuleiro[0] == tabuleiro[1] == tabuleiro[2]:
    print("Jogo acabou")
if tabuleiro[3] == tabuleiro[4] == tabuleiro[5]:
    print("Jogo acabou")
if tabuleiro[6] == tabuleiro[7] == tabuleiro[8]:
    print("Jogo acabou")

# vertical
if tabuleiro[0] == tabuleiro[3] == tabuleiro[6]:
    print("Jogo acabou")
if tabuleiro[1] == tabuleiro[4] == tabuleiro[7]:
    print("Jogo acabou")
if tabuleiro[2] == tabuleiro[5] == tabuleiro[8]:
    print("Jogo acabou")

# diagonal
if tabuleiro[0] == tabuleiro[4] == tabuleiro[8]:
    print("Jogo acabou")
if tabuleiro[2] == tabuleiro[4] == tabuleiro[6]:
    print("Jogo acabou")



# horizontal
for i in range(0, 9, 3):
    if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2]:
        print("Jogo acabou")

# vertical
for i in range(3):
    if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6]:
        print("Jogo acabou")

# diagonal
for i in range(0, 3, 2):
    if tabuleiro[0+i] == tabuleiro[4] == tabuleiro[8-i]:
        print("Jogo acabou")

#######################
for i in range(len(tabuleiro)):
    if i % 3 == 0:
        if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2]:
            print("Jogo acabou")
    if i < 3:
        if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6]:
            print("Jogo acabou")
    if i == 0 or i == 2
        if tabuleiro[0+i] == tabuleiro[4] == tabuleiro[8-i]:
            print("Jogo acabou")


###########
alinhamento = False
vencedor = VAZIO
# horizontal
for i in range(0, 9, 3):
    if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] != VAZIO:
        alinhamento = True
        vencedor = tabuleiro[i]

# vertical
if not alinhamento:
    for i in range(3):
        if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6] != VAZIO:
            alinhamento = True
            vencedor = tabuleiro[i]

# diagonal
if not alinhamento:
    for i in range(0, 3, 2):
        if tabuleiro[0+i] == tabuleiro[4] == tabuleiro[8-i] != VAZIO:
            alinhamento = True
            vencedor = tabuleiro[0+i]

if alinhamento:
    print("Vencedor: ", vencedor)
else:
    if not VAZIO in tabuleiro:
        print("Jogo acabou: Deu Velha!")
