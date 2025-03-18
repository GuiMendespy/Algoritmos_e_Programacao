num=int(input())
count=1
acm=num
while num!=0:
    num=int(input())
    if num==0:
        break
    elif num==-1:
        count+=1
        acm=acm+num
        num+=-1
    else:
        count+=1
        acm=acm+num
        num+=1
print(int(acm/count))