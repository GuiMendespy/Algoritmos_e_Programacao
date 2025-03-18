m1=[]
lista=[]
acm=0
cont=0
for i in range (9):
    num=int(input())
    m1.append(num)
for i in range (len(m1)):
    if m1[i]>0:
        acm+=m1[i]
        cont+=1
lista.append('{:.2f}'.format(acm/cont))
lista.append(min(m1))
if min(m1)%2==0:
    lista.append('1')
else:
    lista.append('0')
acm2=0
acm3=0
for i in range (len(m1)):
    acm2+=m1[i]
for j in range (0,len(m1),4):
    acm3+=m1[j]
lista.append(acm2-acm3)
print(*lista)