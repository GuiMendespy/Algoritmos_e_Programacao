def d(nome):
    r=" "
    for i in nome:
        r+=i
    return r[1::]
num=input().split()
dic={}
lista=[]
for i in range (int(num[0])):
    letras=input().split()
    dic.update({letras[0]:letras[1]})
    dic.update({letras[1]:letras[0]})
for i in range (int(num[1])):
    palavra=list(input())
    for i in palavra:
        if i in dic:
            lista.append(dic.get(i))
        else:
            lista.append(i)
    print(d(lista))
    lista.clear()