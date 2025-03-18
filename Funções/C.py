def calc_vitc(a):
    nomes=[]
    quant=[]
    nomes.append(list(a.keys()))
    quant.append(list(a.values()))
    tab_vitc={'suco':120,'morango':85,'mamao':85,'goiaba':70,'manga':56,'laranja':50,'brocolis':34}
    y=0
    for i in range (n):
        y+=(tab_vitc.get(nomes[0][i]))*int(quant[0][i])
    return y
while True:
    n=int(input())
    dprod={}
    if n==0:
        break
    for i in range (n):
        prod=input().split()
        if i==n:
            break
        dprod[prod[1]]=prod[0]
    k=calc_vitc(dprod)
    if k>130:
        print(f'Menos {k-130} mg')
    elif k<110:
        print(f'Mais {110-k} mg')
    else:
        print(f'{k} mg')