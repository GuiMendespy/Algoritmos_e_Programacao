acm=0
count=0
for i in range (1,8):
    n=int(input())
    count+=1
    acm+=n
    formula=acm/count
if formula<30:
    print('{:.2f}'.format(formula))
    print('Meta atingida')
else:
     print('{:.2f}'.format(formula))