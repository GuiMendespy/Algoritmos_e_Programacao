n=int(input())
lista=[]
acm=0
cont=0
cont1=0
cont2=0
for i in range (n):
    nota=float(input())
    lista.append(nota)
    cont+=1
    acm+=nota
    media=acm/cont
print('{:.2f}'.format(media))
for i in range (n):
    if lista[i] > media+media*0.1:
        cont1+=1
print(cont1)
for i in range (n):
    if lista[i] < media-media*0.1:
        cont2+=1
print(cont2)