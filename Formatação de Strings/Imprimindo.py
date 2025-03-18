n=int(input())
letras=input()
valor1=0
valor2=0
if n==1:
    if 1<=len(letras)<=10:
        valor1=len(letras)*0.75+2
    elif 11<=len(letras)<=30:
        valor1=len(letras)*0.45+2
    elif 31<=len(letras)<=200:
        valor1=len(letras)*0.2+2
if n==2:
    if 1<=len(letras)<=10:
        valor1=len(letras)*0.75+4
    elif 11<=len(letras)<=30:
        valor1=len(letras)*0.45+4
    elif 31<=len(letras)<=200:
        valor1=len(letras)*0.2+4
if n==1:
    if 1<=len(letras)<=10:
        valor2=len(letras)*0.25+6
    elif 11<=len(letras)<=30:
        valor2=len(letras)*0.15+6
    elif 31<=len(letras)<=200:
        valor2=len(letras)*0.1+6
if n==2:
    if 1<=len(letras)<=10:
        valor2=len(letras)*0.25+9
    elif 11<=len(letras)<=30:
        valor2=len(letras)*0.15+9
    elif 31<=len(letras)<=200:
        valor2=len(letras)*0.1+9
if valor1<valor2:
    print(f'A grafica 1 eh a mais em conta')
    print(f'O preco sera: ${valor1:.2f}')
else:
    print(f'A grafica 2 eh a mais em conta')
    print(f'O preco sera: ${valor2:.2f}')