n=int(input())
if n<=0:
    print('0.00')
acm=0
for i in range (1,n+1):
    acm+=1.0/i
print('{:.2f}'.format(acm))