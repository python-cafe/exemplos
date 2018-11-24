X = "X"
O = "O"
VAZIO = " "

tabuleiro = [VAZIO, VAZIO, VAZIO,
             VAZIO, VAZIO, VAZIO,
             VAZIO, VAZIO, VAZIO]
jogada = 0
# tabuleiro = [0, 1, 2,
#              3, 4, 5,
#              6, 7, 8]

jogo_valido = True
vencedor = False

jogador1 = VAZIO
jogador2 = VAZIO

jogador1 = input("Escolha X ou O: ")

if jogador1 == X:
    jogador2 = O
else:
    jogador2 = X

for i in range(0, 9, 3):
    print(i, "|", i+1, "|", i+2, "      ",
        tabuleiro[i], "|", tabuleiro[i+1], "|", tabuleiro[i+2])

while jogo_valido:
    jogada = jogada + 1
    casa = int(input("Escolha onde jogar: "))

    if jogada%2 == 1:
        tabuleiro[casa] = jogador1
    else:
        tabuleiro[casa] = jogador2

    for i in range(0, 9, 3):
        print(i, "|", i+1, "|", i+2, "      ",
            tabuleiro[i], "|", tabuleiro[i+1], "|", tabuleiro[i+2])


    # TODO: verificar se o jogo acabou
    # horizontal
    for i in range(0, 9, 3):
        if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] != VAZIO:
            vencedor = tabuleiro[i]

    # vertical
    if not vencedor:
        for i in range(3):
            if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6] != VAZIO:
                vencedor = tabuleiro[i]

    # diagonal
    if not vencedor:
        for i in range(0, 3, 2):
            if tabuleiro[0+i] == tabuleiro[4] == tabuleiro[8-i] != VAZIO:
                vencedor = tabuleiro[i]

    if vencedor:
        jogo_valido = False
        print("Vencedor: ", vencedor)
    else:
        if not VAZIO in tabuleiro:
            jogo_valido = False
            print("Jogou empatou: Deu velha!")
