frase=list(input())
a=''
lista_i=[]
for i in range (len(frase)):
    lista_i.append(i)
for i in range (len(frase)):
    if i==max(lista_i):
        break
    if frase[i]=='.':
        if frase[i+2]=='4':
            frase.insert(i+2,'A')
            frase.pop(i+2+1)
        if frase[i+2]=='5':
            frase.insert(i+2,'E')
            frase.pop(i+2+1)
        if frase[i+2]=='1':
            frase.insert(i+2,'I')
            frase.pop(i+2+1)
        if frase[i+2]=='0':
            frase.insert(i+2,'O')
            frase.pop(i+2+1)
        if frase[i+2]=='2':
            frase.insert(i+2,'U')
            frase.pop(i+2+1)
for i in range (len(frase)):
    if i==0:
        if frase[i]=='4':
            frase.insert(i,'A')
            frase.pop(i+1)
        if frase[i]=='5':
            frase.insert(i,'E')
            frase.pop(i+1)
        if frase[i]=='1':
            frase.insert(i,'I')
            frase.pop(i+1)
        if frase[i]=='0':
            frase.insert(i,'O')
            frase.pop(i+1)
        if frase[i]=='2':
            frase.insert(i,'U')
            frase.pop(i+1)
    if frase[i]=='4':
        frase.insert(i,'a')
        frase.pop(i+1)
    if frase[i]=='5':
        frase.insert(i,'e')
        frase.pop(i+1)
    if frase[i]=='1':
        frase.insert(i,'i')
        frase.pop(i+1)
    if frase[i]=='0':
        frase.insert(i,'o')
        frase.pop(i+1)
    if frase[i]=='2':
        frase.insert(i,'u')
        frase.pop(i+1)
for i in range (len(frase)):
    if i==0:
        if frase[i]!=' ':
            frase[i]=frase[i].upper()
for i in range (len(frase)):
    if i==max(lista_i):
        break
    if frase[i]=='.':
        if frase[i+2]!=' ':
            frase[i+2]=frase[i+2].upper()

for i in range (len(frase)):
    a+=frase[i]
print(a)