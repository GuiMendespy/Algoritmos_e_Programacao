n=int(input())
m=[]
for i in range (n):
    linha=input().split()
    a=m.append(linha)
acma=0
for i in range (n):
    if i%2==0:
        for j in range (n):
            acma+=int(m[i][j])
acme=0
for i in range (n):
    for j in range (n):
        if j%2!=0:
            acme+=int(m[i][j])
acmr=0
for i in range (n):
        acmr+=int(m[i][i])
if acma>acme and acma>acmr:
    print('Arthur venceu!')
    print('Resultado: {}'.format(acma))
elif acme>acma and acme>acmr :
    print('A entidade venceu!')
    print('Resultado: {}'.format(acme))
elif acmr>acma and acmr>acme:
    print('O intrometido venceu!')
    print('Resultado: {}'.format(acmr))
elif acmr==acme==acma:
    print('Empate!')
    print('Resultado: {}'.format(acma))
elif acma==acme:
    print('Empate!')
    print('Resultado: {}'.format(acma))
elif acma==acmr:
    print('Empate!')
    print('Resultado: {}'.format(acma))
elif acme==acmr:
    print('Empate!')
    print('Resultado: {}'.format(acme))