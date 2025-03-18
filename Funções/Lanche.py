def consulta(lan):
    x=dic.get(lan,0)
    return x
def maior (dicionario):
    y=dicionario[max(dicionario,key=dicionario.get)]
    return y
lanche=input()
dic={}
while lanche.upper()!='FIM':
    retorno=consulta(lanche)
    dic[lanche]=retorno+1
    lanche=input()
a=list(dic.items())
maximo=maior(dic)
for i in range (len(a)):
    if a[i][1]==maximo:
        print(a[i][0],'-',a[i][1])