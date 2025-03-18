acm=0
cont=0
cont2=0
for i in range (10):
    num=int(input())
    cont+=1
    acm+=num
    if num%3==0:
        cont2+=num
media=acm/cont
print('M�dia: {:.1f}'.format(media))
print('Divis�veis: {}'.format(cont2))