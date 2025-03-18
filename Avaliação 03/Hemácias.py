def resultado(sang,sex):
    dic={}
    dic[sang]=sex
    if sex=='M':
        if float(list(dic.keys())[0])<4:
            return 'Baixo'
        elif float(list(dic.keys())[0])>5.4:
            return 'Alto'
        else:
            return 'Normal'
    elif sex=='H':
        if float(list(dic.keys())[0])<4.5:
            return 'Baixo'
        elif float(list(dic.keys())[0])>6.1:
            return 'Alto'
        else:
            return 'Normal'
    elif sex=='C':
        if float(list(dic.keys())[0])<4.07:
            return 'Baixo'
        elif float(list(dic.keys())[0])>5.37:
            return 'Alto'
        else:
            return 'Normal'
    elif sex=='I':
        if float(list(dic.keys())[0])<3.9:
            return 'Baixo'
        elif float(list(dic.keys())[0])>5.36:
            return 'Alto'
        else:
            return 'Normal'
while True:
    hem=input().split()
    if hem==['*']:
        break
    if hem[1]=='M':
        j='Mulher'
    elif hem[1]=='H':
        j='Homem'
    elif hem[1]=='C':
        j='Crianca'
    elif hem[1]=='I':
        j='Idoso'
    print(f'Hemacias {float(hem[0]):.2f}/mm3({j}) = {resultado(hem[0],hem[1])}')