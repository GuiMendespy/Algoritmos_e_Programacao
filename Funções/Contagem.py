n=int(input())
for i in range (n,0,-1):
    lista=[]
    for j in range(i):
        lista.append(str(i))
    j='-'.join(lista)
    print(j)