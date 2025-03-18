def calcular_digito(lista):
    for i in range (2):
        a=lista.index('.')
        lista.pop(a)
    lista1=[]
    lista2=[]
    lista3=[]
    lista1.append(lista[0])
    lista1.append(lista[1])
    lista1.append(lista[2])
    lista2.append(lista[3])
    lista2.append(lista[4])
    lista2.append(lista[5])
    lista3.append(lista[6])
    lista3.append(lista[7])
    lista3.append(lista[8])
    a=max(lista1)
    b=max(lista2)
    c=max(lista3)
    j=int(a)+int(b)+int(c)
    k=j%10
    return k   
while True:
    lista=[]
    dig=input()
    if dig=='FIM':
        break
    lista.extend(dig)
    a=calcular_digito(lista)
    if int(a)==int(lista[-1]):
        print('VALIDO')
    else:
        print('INVALIDO')