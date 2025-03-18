lista=[]
lista_par=[]
lista_imp=[]
for i in range (15):
    num=int(input())
    lista.append(num)
for i in range (len(lista)):
    if lista[i]%2==0:
        lista_par.append(lista[i])
        if len(lista_par)==5:
            for i in range (5):
                print('par[{}] = {}'.format(i,lista_par[i]))
            for i in range(5):
                lista_par.pop(0)      
    else:
        lista_imp.append(lista[i])
        if len(lista_imp)==5:
            for i in range (5):
                print('impar[{}] = {}'.format(i,lista_imp[i]))
            for i in range (5):
                lista_imp.pop(0)
for i in range (len(lista_imp)):
    print('impar[{}] = {}'.format(i,lista_imp[i]))
for i in range (len(lista_par)):
    print('par[{}] = {}'.format(i,lista_par[i]))