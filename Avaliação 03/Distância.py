def distancia(a):
    d=((int(a[1][0])-int(a[0][0]))**2+(int(a[1][1])-int(a[0][1]))**2)**(1/2)
    return d
lista=[]
n1=input().split()
n2=input().split()
lista.append(n1)
lista.append(n2)
print(f'{distancia(lista):.4f}')