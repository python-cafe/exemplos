
### Exemplo 1
conteudo = input("Digite a lista de números (separe com ', ' ): ")
numeros = conteudo.split(", ")
# Não esquecer de converter cada elemento da lista para o tipo de dado desejado
# for i in range(len(numeros)):
#     numeros[i] = int(numeros[i])
numeros = [int(num) for num in numeros]


### Exemplo 2
chave = 3
mensagem = "abacaxi"
# tamanho tabela ASCII
n = 128
# for letra in mensagem:
#     nova_letra = chr((ord(letra) + chave)%n)
#     cifrada = cifrada + nova_letra
lista = [chr((ord(letra) + chave)%n) for letra in mensagem]
cifrada = "".join(lista)
print("abacaxi cifrado resulta em: ", cifrada)


### Exemplo 3
arquivos = [
    '20171124_151321.png', 'Apresentação Python Café.mp4', 'CipherDisk2000.png', 'Constituicao_brasileira_1988.pdf', 'DB.Browser.for.SQLite-3.10.1.dmg', 'DB2018-Full-Report.pdf'
    'Marcas2447.pdf', 'PC11 Repetições I.png', 'Structure-Sensor-3D-scanner.png', 'WhatsApp Image 2018-01-28.png'
    'ambiente_regulatório.png', 'ce5ccffa51698086a6a6d6168affd879.log',
    'defesa_mestrado.pdf', 'hallison_ctd_sbc_v1-rev2.pdf',  'imagens_rgbd_plataformas_moveis.pdf', 'docs.png',
    'kinect.png', 'modelosparapublicaodeartigos.rar'
    ]

imagens = [nome for nome in arquivos if nome.endswith(".png")]
print(imagens)
