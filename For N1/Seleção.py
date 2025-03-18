nomel=[]
idadel=[]
posicaol=[]
count=0
acm=0
for i in range (1,12):
    nome=input()
    if nome=='sair':
        break
    else:
        idade=int(input())
        count+=1
        acm+=idade
        posicao=input()
        posicaol.append(posicao)
        idadel.append(idade)
        nomel.append(nome)
maior=idadel.index(max(idadel))
menor=idadel.index(min(idadel))
print(nomel[menor])
print(posicaol[maior])
print('{:.1f}'.format(acm/count))