nome_ving=input()
if nome_ving not in ("Homem de Ferro","Hulk", "Capit�o Am�rica", "Thor", "Gavi�o Arqueiro",  "Vi�va Negra"):
    print("Vingador Inv�lido")
else:
    poder=input()
    energia=int(input())
    if nome_ving == "Homem de Ferro" and poder!= "Armadura de Ferro":
       print(nome_ving,"NAO conseguiu derrotar Thanos")
       if poder=="For�a Bruta":
        print("Esse � o poder do Hulk")
       elif poder=="Escudo":
        print("Esse � o poder do Capit�o Am�rica")
       elif poder=="Martelo":
        print("Esse � o poder do Thor")
       elif poder=="Arco e Flecha":
        print("Esse � o poder do Gavi�o Arqueiro")
       elif poder=="Intelig�ncia":
        print("Esse � o poder da Vi�va Negra")
    elif nome_ving=="Hulk" and poder!="For�a Bruta":
       print(nome_ving,"NAO conseguiu derrotar Thanos")
       if poder=="Armadura de Ferro":
        print("Esse � o poder do Homem de Ferro")
       elif poder=="Escudo":
        print("Esse � o poder do Capit�o Am�rica")
       elif poder=="Martelo":
        print("Esse � o poder do Thor")
       elif poder=="Arco e Flecha":
        print("Esse � o poder do Gavi�o Arqueiro")
       elif poder=="Intelig�ncia":
        print("Esse � o poder da Vi�va Negra")
    elif nome_ving=="Capit�o Am�rica" and poder!= "Escudo":
       print(nome_ving,"NAO conseguiu derrotar Thanos")
       if poder=="For�a Bruta":
        print("Esse � o poder do Hulk")
       elif poder=="Armadura de Ferro":
        print("Esse � o poder do Homem de Ferro")
       elif poder=="Martelo":
        print("Esse � o poder do Thor")
       elif poder=="Arco e Flecha":
        print("Esse � o poder do Gavi�o Arqueiro")
       elif poder=="Intelig�ncia":
        print("Esse � o poder da Vi�va Negra")
    elif nome_ving=="Thor" and poder!="Martelo":
       print(nome_ving,"NAO conseguiu derrotar Thanos")
       if poder=="Escudo":
        print("Esse � o poder do Capit�o Am�rica")
       elif poder=="For�a Bruta":
        print("Esse � o poder do Hulk")
       elif poder=="Armadura de Ferro":
        print("Esse � o poder do Homem de Ferro")
       elif poder=="Arco e Flecha":
        print("Esse � o poder do Gavi�o Arqueiro")
       elif poder=="Intelig�ncia":
        print("Esse � o poder da Vi�va Negra")
    elif nome_ving=="Gavi�o Arqueiro" and poder!= "Arco e Flecha":
       print(nome_ving,"NAO conseguiu derrotar Thanos")
       if poder=="Martelo":
        print("Esse � o poder do Thor")
       elif poder=="Escudo":
        print("Esse � o poder do Capit�o Am�rica")
       elif poder=="For�a Bruta":
        print("Esse � o poder do Hulk")
       elif poder=="Armadura de Ferro":
        print("Esse � o poder do Homem de Ferro")
       elif poder=="Intelig�ncia":
        print("Esse � o poder da Vi�va Negra")
    elif nome_ving=="Vi�va Negra" and poder!="Intelig�ncia":
       print(nome_ving,"NAO conseguiu derrotar Thanos")
       if poder=="Arco e Flecha":
        print("Esse � o poder do Gavi�o Arqueiro")
       if poder=="Martelo":
        print("Esse � o poder do Thor")
       elif poder=="Escudo":
        print("Esse � o poder do Capit�o Am�rica")
       elif poder=="For�a Bruta":
        print("Esse � o poder do Hulk")
       elif poder=="Armadura de Ferro":
        print("Esse � o poder do Homem de Ferro")
    elif nome_ving=="Homem de Ferro" and poder=="Armadura de Ferro" and energia > 10:
        print(nome_ving,"conseguiu derrotar Thanos")
    elif nome_ving=="Hulk" and poder=="For�a Bruta" and energia>5:
        print(nome_ving,"conseguiu derrotar Thanos")
    elif nome_ving=="Capit�o Am�rica" and poder=="Escudo" and energia > 7:
        print(nome_ving,"conseguiu derrotar Thanos")
    elif nome_ving=="Thor" and poder=="Martelo" and energia >4:
        print(nome_ving,"conseguiu derrotar Thanos")
    elif nome_ving=="Gavi�o Arqueiro" and poder=="Arco e Flecha" and energia>12:
        print(nome_ving,"conseguiu derrotar Thanos")
    elif nome_ving=="Vi�va Negra" and poder=="Intelig�ncia" and energia>20:
        print(nome_ving,"conseguiu derrotar Thanos")
    else:
        print(nome_ving,"NAO conseguiu derrotar Thanos, chamem outro Vingador")