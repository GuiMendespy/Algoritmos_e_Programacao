n=int(input())
count=0
acumulador=0
parar=0
while count<20:
    a=int(input())
    count+=1
    if a==n and parar == 0:
        acumulador+=1
    if a==-1:
        parar = 1
print(n,'aparece',acumulador,'vezes')