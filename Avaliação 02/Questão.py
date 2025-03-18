n=input()
w=n.replace(',',' ')
x=w.split()
cont=0
for i in range (len(x)):
    if x[i].endswith('ar'):
        cont+=1
    elif x[i].endswith('er'):
        cont+=1
    elif x[i].endswith('ir'):
        cont+=1
    elif x[i].endswith('or'):
        cont+=1
    else:
        x.insert(i,'')
        x.pop(i+1)
print('temos {} palavra(s) no infitivo.'.format(cont))
k=' '.join(x)
x=k.split()
for i in range (len(x)):
    if x[i].endswith('ar'):
        g=str(x[i]).replace('ar','ando')
        p=str(x[i]).replace('ar','ado')
        v='a'
        r=str(x[i]).replace('ar','')
        gera='primeira'
        print('o verbo {} no Ger�ndio �: {}'.format(x[i],g))
        print('o verbo {} no Partic�pio �: {}'.format(x[i],p))
        print('a vogal tem�tica do verbo {} � {}'.format(x[i],v))
        print('o radical do verbo {} � {}'.format(x[i],r))
        print('O verbo {} � da {} conjuga��o.'.format(x[i],gera))
        if i+1==cont:
            continue
        else:
            print()
    elif x[i].endswith('er'):
        g=str(x[i]).replace('er','endo')
        p=str(x[i]).replace('er','ido')
        v='e'
        r=str(x[i]).replace('er','')
        gera='segunda'
        print('o verbo {} no Ger�ndio �: {}'.format(x[i],g))
        print('o verbo {} no Partic�pio �: {}'.format(x[i],p))
        print('a vogal tem�tica do verbo {} � {}'.format(x[i],v))
        print('o radical do verbo {} � {}'.format(x[i],r))
        print('O verbo {} � da {} conjuga��o.'.format(x[i],gera))
        if i+1==cont:
            continue
        else:
            print()
    elif x[i].endswith('ir'):
        g=str(x[i]).replace('ir','indo')
        p=str(x[i]).replace('ir','ido')
        v='i'
        r=str(x[i]).replace('ir','')
        gera='terceira'                                              
        print('o verbo {} no Ger�ndio �: {}'.format(x[i],g))
        print('o verbo {} no Partic�pio �: {}'.format(x[i],p))
        print('a vogal tem�tica do verbo {} � {}'.format(x[i],v))
        print('o radical do verbo {} � {}'.format(x[i],r))
        print('O verbo {} � da {} conjuga��o.'.format(x[i],gera))
        if i+1==cont:
            continue
        else:
            print()
    elif x[i].endswith('or'):
        g=str(x[i]).replace('or','ondo')
        p=str(x[i]).replace('or','osto')
        v='o'
        r=str(x[i]).replace('or','')
        gera='segunda'                                              
        print('o verbo {} no Ger�ndio �: {}'.format(x[i],g))
        print('o verbo {} no Partic�pio �: {}'.format(x[i],p))
        print('a vogal tem�tica do verbo {} � {}'.format(x[i],v))
        print('o radical do verbo {} � {}'.format(x[i],r))
        print('O verbo {} � da {} conjuga��o.'.format(x[i],gera))
        if i+1==cont:
            continue
        else:
            print()