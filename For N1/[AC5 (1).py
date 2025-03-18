quant=int(input())
count=0
acm=0
for i in range (quant):
    nota=int(input())
    count+=1
    acm+=nota
print(round(acm/count,1))