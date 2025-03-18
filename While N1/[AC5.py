num=int(input())
sn=0
while num>0:
    digito=num%10
    sn+=digito
    num=num//10
print(sn)