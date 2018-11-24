from criptografia import criptografar, cifrardoc, descriptografar, decifrardoc
from tkinter.filedialog import askopenfilename

tarefa = int(input("Escolha uma tarefa: \n1- Cifrar texto \n2 - Cifrar documento; \n3 - Decifrar Texto \n4 - Decifrar documento \n9 - Sair\n"))
continuar = True
while continuar:
    if tarefa == 1:
        #cifrar texto
        msg = input("Digite a mensagem a ser cifrada: ")
        chave = int(input("Digite a chave de criptografia: "))
        cifrada = criptografar(msg, chave)
        print("Mensagem cifrada: ", cifrada)
    elif tarefa == 2:
        #cifrar documento
        # fonte = input("Digite o endereço do documento a ser cifrado: ")
        fonte = askopenfilename()
        destino = input("Digite o endereço do documento de destino: ")
        chave = int(input("Digite a chave de criptografia: "))
        cifrardoc(fonte, destino, chave)
        print("Documento cifrado com sucesso!")
    elif tarefa == 3:
        #decifrar texto
        msg = input("Digite a mensagem a ser decifrada: ")
        chave = int(input("Digite a chave de criptografia: "))
        decifrada = descriptografar(msg, chave)
        print("Mensagem decifrada: ", decifrada)
    elif tarefa == 4:
        #decifrar documento
        fonte = input("Digite o endereço do documento a ser decifrado: ")
        destino = input("Digite o endereço do documento de destino: ")
        chave = int(input("Digite a chave de criptografia: "))
        decifrardoc(fonte, destino, chave)
        print("Documento decifrado com sucesso!")
    elif tarefa == 9:
        continuar = False
        print("Fechando o programa")
    else:
        print("Opção Inválida. Digite Novamente")
    tarefa = int(input("Escolha uma tarefa: \n1- Cifrar texto \n2 - Cifrar documento; \n3 - Decifrar Texto \n4 - Decifrar documento \n9 - Sair"))
