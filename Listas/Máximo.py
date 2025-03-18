lista=[]
n=int(input())
for i in range (n):
    num=int(input())
    lista.append(num)
    lista.sort()
count1=lista.count(lista[n-1])
count2=lista.count(lista[0])
print('Maior: {} apareceu {} vezes'.format(lista[n-1],count1))
print('Menor: {} apareceu {} vezes'.format(lista[0],count2))