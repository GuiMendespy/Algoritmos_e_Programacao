n1=int(input())
n2=int(input())
if n2<=n1:
    while n2<=n1:
        print('Digite um valor maior que o primeiro!')
        n2=int(input())
acm=0
while n1<=n2:
    if n1==2:
        acm=acm+n1
    if n1==3:
        acm=acm+n1
    if n1==5:
        acm=acm+n1
    if n1==7:
        acm=acm+n1
    if n1%2!=0:
        if n1%3!=0:
            if n1%5!=0:
                if n1%7!=0:
                    acm=acm+n1
    n1+=1
if acm==0:
    print('Sem numeros primos no intervalo informado.')
else:
    print(acm)