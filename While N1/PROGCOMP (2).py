a=float(10000)
b=float(5000)
i=0
while a>=b:
    a=float(10000+100*i)
    b=float(5000+300*i)
    print('{:.2f}'.format(a-b))
    if a==b:
        break
    i+=1
    