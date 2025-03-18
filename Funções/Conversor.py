def bina(lista):
    soma=[]
    for i in range (len(lista)):
        lista_elev=[]
        for j in range (8):
            a=2**j
            b=(int(lista[i][j])*a)
            lista_elev.append(b)
        c=sum(lista_elev)
        soma.append(c)
    d=''
    for i in range (len(soma)):
        if i==len(soma)-1:
            d+=(str(soma[i]))
        else:
            d+=(str(soma[i])+'.')
    return d
lista=[]
for i in range (4):
    n=input()
    k=n.split()
    lista.append(k)
for i in range (len(lista)):
    lista[i].reverse()
print(bina(lista))