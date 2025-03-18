n=int(input())
matriculas=[]
nomes=[]
notas=[]
acm=0
for i in range (n):
    matri=int(input())
    matriculas.append(matri)
    nome=input()
    nomes.append(nome)
    nota=float(input())
    notas.append(nota)
    acm+=nota
    media=acm/n
notas_acima=[]
matriculas_acima=[]
nomes_acima=[]
for i in range (n):
    if notas[i]>media:
        if notas[i] not in notas_acima:
            notas_acima.append(notas[i])
            matriculas_acima.append(matriculas[i])
            nomes_acima.append(nomes[i])
        elif matriculas[i]<matriculas[i-1]:
            notas_acima.insert(i-1,notas[i])
            matriculas_acima.insert(i-1,matriculas[i])
            nomes_acima.insert(i-1,nomes[i])
        else:
            notas_acima.append(notas[i])
            matriculas_acima.append(matriculas[i])
            nomes_acima.append(nomes[i])
for i in range (1,len(notas_acima)):
    if notas_acima[i]<notas_acima[i-1]:
        notas_acima.insert(i-1,notas_acima[i])
        matriculas_acima.insert(i-1,matriculas_acima[i])
        nomes_acima.insert(i-1,nomes_acima[i])
        notas_acima.pop(i+1)
        matriculas_acima.pop(i+1)
        nomes_acima.pop(i+1)
for i in range (len(notas_acima)-1,0,-1):
    if notas_acima[i]<notas_acima[i-1]:
        notas_acima.insert(i-1,notas_acima[i])
        matriculas_acima.insert(i-1,matriculas_acima[i])
        nomes_acima.insert(i-1,nomes_acima[i])
        notas_acima.pop(i+1)
        matriculas_acima.pop(i+1)
        nomes_acima.pop(i+1)

for i in range (1,len(notas_acima)):
    if  notas_acima[i]==notas_acima[i-1]:
        if matriculas_acima[i]<matriculas_acima[i-1]:
            notas_acima.insert(i-1,notas_acima[i])
            matriculas_acima.insert(i-1,matriculas_acima[i])
            nomes_acima.insert(i-1,nomes_acima[i])
            notas_acima.pop(i+1)
            matriculas_acima.pop(i+1)
            nomes_acima.pop(i+1)
for i in range (len(notas_acima)-1,0,-1):
    if  notas_acima[i]==notas_acima[i-1]:
        if matriculas_acima[i]<matriculas_acima[i-1]:
            notas_acima.insert(i-1,notas_acima[i])
            matriculas_acima.insert(i-1,matriculas_acima[i])
            nomes_acima.insert(i-1,nomes_acima[i])
            notas_acima.pop(i+1)
            matriculas_acima.pop(i+1)
            nomes_acima.pop(i+1)
for i in range (len(notas_acima)):
        print(f'Matricula: {matriculas_acima[i]} Nome: {nomes_acima[i]} Nota: {notas_acima[i]}')
print(f'Media = {media:.2f}')