X = "X"
O = "O"
VAZIO = " "

jogo_valido = True
vencedor = VAZIO
jogadas = 0
tabuleiro = [VAZIO, VAZIO, VAZIO,
             VAZIO, VAZIO, VAZIO,
             VAZIO, VAZIO, VAZIO]

jogador1 = input("Escolha X ou O: ")
if jogador1 == X:
    jogador2 = O
else:
    jogador2 = X

for i in range(0, 9, 3):
    print(i, "|", i+1, "|", i+2,
    "       ", tabuleiro[i], "|", tabuleiro[i+1], "|", tabuleiro[i+2])
while jogo_valido:
    jogadas = jogadas+1
    casa = int(input("Escolha onde jogar: "))
    if jogadas%2 == 1:
        tabuleiro[casa] = jogador1
    else:
        tabuleiro[casa] = jogador2

    for i in range(0, 9, 3):
        print(i, "|", i+1, "|", i+2,
        "       ", tabuleiro[i], "|", tabuleiro[i+1], "|", tabuleiro[i+2])

    # horizontal
    for i in range(0, 9, 3):
        if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] != VAZIO:
            vencedor = tabuleiro[i]
    # vertical
    if vencedor == VAZIO:
        for i in range(3):
            if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6] != VAZIO:
                vencedor = tabuleiro[i]
    # diagonal
    if vencedor == VAZIO:
        for i in range(0, 3, 2):
            if tabuleiro[0+i] == tabuleiro[4] == tabuleiro[8-i] != VAZIO:
                vencedor = tabuleiro[i]

    if vencedor != VAZIO:
        print("Vencedor: ", vencedor)
        jogo_valido = False
    else:
        if not VAZIO in tabuleiro:
            print("Jogou empatou: Deu velha!")
            jogo_valido = False
