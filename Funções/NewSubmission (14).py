def baralho(a):
    for i in range (len(a)):
        for j in range (1):
            if a[i][j]==a[i][j+1]==a[i][j+2]:
                a[i].pop(j)
                a[i].pop(j)
            elif int(a[i][j])+1==int(a[i][j+1])==(int(a[i][j+2])-1):
                a[i].pop(j+1)
                a[i].pop(j+1)
            elif a[i][j]==a[i][j+1]<a[i][j+2]:
                f=soma(a)
                a[i].pop(j)
                a[i].pop(j+1)
                a[i].append(int(a[i][0])//2)
                a[i].pop(0)
            elif a[i][j]>a[i][j+1]==a[i][j+2]:
                f=soma(a)
                a[i].pop(j)
                a[i].pop(j+1)
                a[i].append(int(a[i][0])//2)
                a[i].pop(0)
            elif a[i][j]==a[i][j+1]>a[i][j+2]:
                f=soma(a)
                a[i].pop(j)
                a[i].pop(j+1)
                a[i].append(int(a[i][0])//2)
                a[i].pop(0)
            elif a[i][j]<a[i][j+1]==a[i][j+2]:
                f=soma(a)
                a[i].pop(j)
                a[i].pop(j+1)
                a[i].append(int(a[i][0])//2)
                a[i].pop(0)
            else:
                f=soma(a)
                a[i].append(0)
                a[i].pop(0)
                a[i].pop(0)
                a[i].pop(0)
    if sum(a[0])==sum(a[1]):
        return '0'
    elif sum(a[0])>sum(a[1]):
        return '1'
    elif sum(a[0])<sum(a[1]):
        return '2'
def soma(a):
    for i in range (2):
        for j in range (1):
            if len(a[i])==3:
                if int(a[i][j])+int(a[i][j+1])+int(a[i][j+2])==8:
                        k=8
                        a[i].append(k)
    return a
lista=[]
for i in range (2):
    n=lista.append(input().split())
    for j in range (3):
        lista[i].append(int(lista[i][j]))
    lista[i].pop(0)
    lista[i].pop(0)
    lista[i].pop(0)
lista[0].sort()
lista[1].sort()
print(baralho(lista))