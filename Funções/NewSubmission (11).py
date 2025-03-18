def EstacaoAno(dia,mes):
    if mes == 1 or mes==2:
        j='VERAO'
        return j
    elif mes==4 or mes==5:
        j='OUTONO'
        return j
    elif mes==7 or mes==8 :
        j='INVERNO'
        return j
    elif mes==10 or mes==11:
        j='PRIMAVERA'
        return j
    elif mes==3 and dia<=20:
        j='VERAO'
        return j
    elif mes==3 and dia>=21:
        j='OUTONO'
        return j
    elif mes==6 and dia<=20:
        j='OUTONO'
        return j
    elif mes==6 and dia>=21:
        j='INVERNO'
        return j
    elif mes==9 and dia<=20:
        j='INVERNO'
        return j
    elif mes==9 and dia>=21:
        j='PRIMAVERA'
        return j
    elif mes==12 and dia<=20:
        j='PRIMAVERA'
        return j
    elif mes==12 and dia>=21:
        j='VERAO'
        return j
dia=int(input())
mes=int(input())
print(EstacaoAno(dia,mes))