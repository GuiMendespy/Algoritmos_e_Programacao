nome = list(input().lower())
chave = int(input())
a=""
nomes=[]
cript=[]
alfab=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in nome:
    nomes.append(i)
    if i in alfab:
        j= alfab.index(i) + chave
        k= cript.append(alfab[j])
for i in cript:
    a+=i
print(a)