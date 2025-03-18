frase=list(input())
lista=[]
a=''
for i in range (len(frase)-1,-1,-1):
        if frase[i]!=' ':
            lista.append(frase[i])
        else:
            break
lista.reverse()
for i in range(len(lista)):
    a+=lista[i]
print(a)