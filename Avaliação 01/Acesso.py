acm_adul=0
acm_crian=0
n=int(input())
while True:
    n_adul=int(input())
    if n_adul<0:
        break
    acm_adul+=n_adul
    n_crian=int(input())
    acm_crian+=n_crian
    n_crian_conv=int(input())
    acm_crian+=n_crian_conv
    if acm_crian<=n:
        print('Acesso permitido!')
        print('Adultos na piscina:',acm_adul)
        print('Criancas na piscina:',acm_crian)
        print('***')
    if acm_crian>n:
        if n_crian_conv>0:
            print('Acesso permitido devido a presenca de convidado(s).')
            print('Adultos na piscina:',acm_adul)
            print('Criancas na piscina:',acm_crian)
            print('***')
        if n_crian>0 and n_crian_conv==0:
            print('Capacidade maxima de criancas atingida/excedida.')
            print('Tem {} crianca(s) a mais que as {} permitidas.'.format(acm_crian-n-n_crian,n))
            print('Adultos na piscina:',acm_adul-n_adul)
            print('Criancas na piscina:',acm_crian-n_crian)
            print('***')
            acm_crian=acm_crian-n_crian
            acm_adul=acm_adul-n_adul
        if n_adul>0 and n_crian_conv==0 and n_crian==0:
            print('Acesso permitido!')
            print('Adultos na piscina:',acm_adul)
            print('Criancas na piscina:',acm_crian)
            print('***')