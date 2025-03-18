n=1
cent=0
dez=0
unidade=0
while n!=0:
    num=int(input())
    if num==0:
        break
    if num<1 or num>999:
        print('n�mero invalido, digite n�meros de 1 a 999')
    else:
        cent=num//100
        dez=(num%100)//10
        unidade=(num%100)%10
        print('O n�mero tem :',cent,'centenas')
        print('O n�mero tem :',dez,'dezenas')
        print('O n�mero tem :',unidade,'unidades')
        if cent==0 and unidade==0:
            print('O n�mero invertido �:  {}'.format(dez))
        elif cent==0:
            print('O n�mero invertido �:  {}{}'.format(unidade,dez))
        elif dez==0 and unidade==0:
            print('O n�mero invertido �:  {}'.format(cent))
        elif unidade==0:
            print('O n�mero invertido �:  {}{}'.format(dez,cent))
        else:
            print('O n�mero invertido �:  {}{}{}'.format(unidade,dez,cent))
    n+=1