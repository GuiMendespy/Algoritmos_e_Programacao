a1=int(input())
a2=int(input())
a3=int(input())
if (a1<90) and (a2<90) and (a3<90):
    print("Digite o valor do primeiro �ngulo:")
    print("Digite o valor do segundo �ngulo:")
    print("Digite o valor do terceiro �ngulo:")
    print("Este e um triangulo acutangulo.")
if (a1==90) or (a2==90) or (a3==90):
    print("Digite o valor do primeiro �ngulo:")
    print("Digite o valor do segundo �ngulo:")
    print("Digite o valor do terceiro �ngulo:")
    print("Este e um triangulo retangulo.")
if (a1>90) or (a2>90) or (a3>90):
    print("Digite o valor do primeiro �ngulo:")
    print("Digite o valor do segundo �ngulo:")
    print("Digite o valor do terceiro �ngulo:")
    print("Este e um triangulo obtusangulo.")