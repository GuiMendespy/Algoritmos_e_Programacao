dic={'a':'@','A':'@','e':'3','E':'3','i':'1','I':'1','o':'0','O':'0','t':'7','T':'7','s':'5','S':'5'}
lista=[]
def d(nome):
    r=" "
    for i in nome:
        r+=i
    t=len(r[::-1])
    r=r[::-1]
    r=r[0:t-1]
    return (r)
pala=list(input())
if '1' in pala or '2' in pala or '3' in pala or '4' in pala or '5' in pala or '6' in pala or '7' in pala or '8' in pala or '9' in pala or '0' in pala:
    print("numeros")
    print(0)
else:
    cont=0
    for i in pala:
        if i in dic:
            cont+=1
            lista.append(dic.get(i))
        else:
            lista.append(i)
    print(d(lista))
    print(cont)