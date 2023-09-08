qte=int(input("Digite a quantidade de minutos:"))
while qte<1:
    qte=int(input("Digite a quantidade de minutos:"))
if qte<=100:
    print("Valor a pagar: R$50,00")
else:
    total=((qte-100)*2)+50
    print("Valor a pagar: R$",total,",00")