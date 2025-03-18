n=int(input())
lista=[]
lista_fat=[]
for i in range (n):
    num=int(input())
    lista.append(num)
for elemento in lista:
    print(elemento, end=' ')

print()
for i in (lista):
    x=1
    for j in range (1,i+1):
        x*=j
    lista_fat.append(x)
for fatorial in lista_fat:
    print(fatorial, end=' ')