situacao_disc="Z"
acm1=0
acm2=0
p=int(input())
if p<=0 or p>10:
        print('entrada invalida')
elif 0<p<10:
    while 0<p<10:
        ch=int(input())
        nota=int(input())
        situacao_disc=str(input())
        p=int(input())
        if (situacao_disc== 'A' or situacao_disc== 'R' or situacao_disc== 'RF') and (ch==33 or ch==50 or ch==67 or ch==83):
            acm1+=nota*ch
            acm2+=ch
        if p<=0 or p>10:
            break
        p+=1
    if acm2 ==0:
        print('entrada invalida')
    elif situacao_disc== 'A' or situacao_disc== 'R' or situacao_disc== 'RF' or situacao_disc== 'DT' or situacao_disc=='AD' or situacao_disc=='DE' or situacao_disc== 'AE' or situacao_disc== 'DD' or situacao_disc== 'DC':
            f1=acm1/acm2
            print('{:.2f}'.format(f1))
    else:
        print('entrada invalida')