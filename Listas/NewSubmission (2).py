n=int(input())
cont_par=0
cont_imp=0
acm_par=0
acm_imp=0
lista=[]
for i in range (n):
    fig=int(input())
    if fig%2==0:
        cont_par+=1
    else:
        cont_imp+=1
    if fig not in lista:
        lista.append(fig)
for i in range (len(lista)):
    if lista[i]%2==0:
        acm_par+=lista[i]
    else:
        acm_imp+=lista[i]
print(cont_par)
print(cont_imp)
if acm_par>acm_imp:
    print(acm_par)
else:
    print(acm_imp)