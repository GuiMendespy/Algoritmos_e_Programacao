lista_notas=[]
cont=0
acm=0
n=int(input())
if n>0:
    for i in range (n):
        nota=float(input())
        acm+=nota
        cont+=1
        lista_notas.append(nota)
    for i in range (n):
        print('Nota {}: {}'.format(i+1,lista_notas[i]))
    print('Media: {:.2f}'.format(acm/cont))
else:
    print('Numero de notas invalido.')