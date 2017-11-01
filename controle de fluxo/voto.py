# Quantos anos você tem?
# idade
# Se idade < 16 então
# - Você não pode votar
idade = int(input("Quantos anos você tem?\n"))
if idade < 16:
    print("Você não pode votar!")
elif idade < 18:
    print("Você pode votar, mas é facultativo")
elif idade < 70:
    print("Você é obrigado a votar!")
else:
    print("Você não é mais obrigado a votar, é facultativo")


print("FIM")
