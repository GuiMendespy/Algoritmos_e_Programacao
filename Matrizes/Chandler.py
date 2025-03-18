n=int(input())
lista=[]
m1=[]
m2=[]
m3=[]
m4=[]
for i in range (n):
    linha=input()
    a=linha.split()
    lista.append(a)
for i in range (len(lista)):
    for j in range (len(lista)):
        if int(lista[i][j])<0:
            e=int(lista[i][j])*2
            k=str(e)
            m1.append(k)
        else:
            m1.append(lista[i][j])
for i in range (0,len(m1),n):
    sub=m1[i:i+n]
    m2.append(sub)
for i in range (len(m2)):
    for j in range (len(m2)):
        m3.append(m2[j][i])
for i in range (0,len(m3),n):
    sub=m3[i:i+n]
    m4.append(sub)
for i in range (len(m4)):
    print(*m4[i])