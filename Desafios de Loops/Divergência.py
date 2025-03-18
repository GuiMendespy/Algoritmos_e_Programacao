n=int(input())
for i in range (1,n+1):
    if i%7==0 and i%2==0:
        i+=1
    else:
        print(i)