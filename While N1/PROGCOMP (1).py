num=float(input())
acm=num
count=1
while num!=-1:
    num=float(input())
    if num==-1:
        break
    acm=acm+num
    count+=1
    num+=1
print('{:.2f}'.format(acm/count))