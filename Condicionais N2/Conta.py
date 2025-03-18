conta=int(input())
f1=7
f2=1*(conta-10)+f1
f3=2*(conta-30)+27
f4=(5*(conta-100))+140+27
if conta<0:
    print("Digite o consumo de agua em m3:")
    print("Numeros negativos nao sao aceitos.")
if conta>0 and conta<=10:
    print("Digite o consumo de agua em m3:")
    print("O valor a ser pago e de R$ {}.".format(f1))
if 11<=conta<=30:
    print("Digite o consumo de agua em m3:")
    print("O valor a ser pago e de R$ {}.".format(f2))
if 31<=conta<=100:
    print("Digite o consumo de agua em m3:")
    print("O valor a ser pago e de R$ {}.".format(f3))
if conta>=101:
    print("Digite o consumo de agua em m3:")
    print("O valor a ser pago e de R$ {}.".format(f4))
