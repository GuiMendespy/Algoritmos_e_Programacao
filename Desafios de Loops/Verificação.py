n=1
while n!=0:
    idade=int(input())
    if idade==0:
        break
    if 18<=idade<=70:
        print('Voc� tem a obrigatoriedade de votar.')
    elif idade<0:
        print('Voc� ainda n�o nasceu.')
    elif idade<16:
        print('Voc� n�o pode votar.')
    elif 16<=idade<=17:
        print('Na sua idade, o voto � opcional.')
    elif idade>70:
        print('Na sua idade, o voto � opcional.')
    n+=1