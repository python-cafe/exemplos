X = "X"
O = "O"
VAZIO = " "

# tabuleiro = [0, 1, 2,
#              3, 4, 5,
#              6, 7, 8]

# tabuleiro = [X, O, X,
#              O, X, O,
#              O, VAZIO, X]

# tabuleiro = [VAZIO, VAZIO, VAZIO,
#              VAZIO, VAZIO, VAZIO,
#              VAZIO, VAZIO, VAZIO]
#
# tabuleiro = [X, O, X,
#              X, X, VAZIO,
#              O, O, O]
#
tabuleiro = [X, O, X,
             O, X, O,
             O, X, O]

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
            vencedor = tabuleiro[i]

if alinhamento:
    print("Vencedor: ", vencedor)
else:
    if not VAZIO in tabuleiro:
        print("Jogou empatou: Deu velha!")
