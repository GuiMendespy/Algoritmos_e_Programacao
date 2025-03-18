conta=0
conte=0
conti=0
conto=0
contu=0
frase=list(input())
for i in range (len(frase)):
    if frase[i]=='A' or frase[i]=='a':
        conta+=1
    elif frase[i]=='E' or frase[i]== 'e':
        conte+=1
    elif frase[i]=='I' or frase[i]== 'i':
        conti+=1
    elif frase[i]=='O' or frase[i]== 'o':
        conto+=1
    elif frase[i]=='U' or frase[i]== 'u':
        contu+=1
print(f'a {conta}')
print(f'e {conte}')
print(f'i {conti}')
print(f'o {conto}')
print(f'u {contu}')
print('{:.2f}%'.format(((conta+conte+conti+conto+contu)/len(frase))*100))