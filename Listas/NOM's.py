n=int(input())
lista_notas=[]
lista_pesos=[]
j=0
y=0
for i in range (n):
    nota=float(input())
    lista_notas.append(nota)
for i in range (n):
    peso=float(input())
    lista_pesos.append(peso)
    y=sum(lista_pesos)
for i in range (n):
    j+=lista_notas[i]*lista_pesos[i]/y
print('{:.2f}'.format(j))