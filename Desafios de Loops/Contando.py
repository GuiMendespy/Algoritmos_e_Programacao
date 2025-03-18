count=0
quant=int(input())
for i in range (1, quant+1):
    num=int(input())
    num=str(num)
    for i in num:
        num2=int(i)
        if num2 == 2 or num2==3 or num2==5 or num2==7:
            count+=1
    print('Prime digits:',count)
    count=0