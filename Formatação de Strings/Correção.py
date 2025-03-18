n=int(input())
gab=list(input())
provas=int(input())
for j in range (provas):
    cont=0
    qts=list(input())
    for i in range (n):
        if qts[i]==gab[i]:
            cont+=1
    print(cont)