while True:
    num=int(input())
    if num==0:
        break
    a=(num/2+0.5)**2
    b=((num/2+0.5)-1)**2
    print('{:.0f}'.format(a),'-','{:.0f}'.format(b))
    num+=1