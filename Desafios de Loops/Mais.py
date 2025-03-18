acm=0
n=int(input())
for i in range (1,n+1):
    denominador1= (n*4)
    denominador2= ((n*4)-2)
    if i==1:
        matriz=i/(denominador1*denominador2)
        acm+=matriz
    if i>1:
        denominador= (denominador1-4*(i-1)) * (denominador2-4*(i-1))
        matriz=i/denominador
        acm+=matriz
print('{:.4f}'.format(acm))