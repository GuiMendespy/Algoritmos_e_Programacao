acm=0
nomel=[]
valorl=[]
valor_total=float(input())
p=int(input())
if p==0:
    print('Nao ha conta ou funcionario suficiente para pagar a conta')
else:
    for i in range (1,p+1):
        nome=input()
        valor=float(input())
        nomel.append(nome)
        valorl.append(valor)
        acm+=valor
    maior_valor=valorl.index(max(valorl))
    maior_nome_valor=valorl.index(max(valorl))
    print(nomel[maior_nome_valor],'pagou R$',valorl[maior_valor])
    if acm<valor_total:
        print('Valor insuficiente: falta R$ ',valor_total-acm)
    else:
        print('Valor excedente: sobra R$ ',acm-valor_total)