lista1=[]
lista2=[]
n=int(input())
if n>0:
    for i in range (n):
        num1=int(input())
        lista1.append(num1)
    n=int(input())
    if n>0:
        for i in range (n):
            num2=int(input())
            lista2.append(num2)
        print(*lista1,*lista2)
    else:
        print('Erro - A lista deve ter pelo menos 1 elemento.')
else:
    print('Erro - A lista deve ter pelo menos 1 elemento.')