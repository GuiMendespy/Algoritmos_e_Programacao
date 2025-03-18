from collections import Counter
gab=input()
lpont=[]
acm=0
cont=0
while True:
    aluno=input()
    if aluno=='9999':
        break
    cont+=1
    pont=0
    b=aluno.find(' ')
    for i in range (len(gab)):
        if aluno[b+1+i]==gab[i]:
            pont+=1
    lpont.append(pont)
for i in range (cont):
    print(i+1,'{:.1f}'.format(lpont[i]))
for i in range (len(lpont)):
    if lpont[i]>=6:
        acm+=1
print('{:.1f}%'.format((acm/cont)*100))
contagem = Counter(lpont)
valor_mais=contagem.most_common(1)[0][0]
print('{:.1f}'.format(valor_mais))