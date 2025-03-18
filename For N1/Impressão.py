while True:
    num1=int(input())
    if num1>9 or num1<1:
        print("Insira um n�mero inicial entre 1 e 9")
    if 1<=num1<=9:
        break
    else:
            num1+=1
while True:
    num2=int(input())
    if num2>9 or num2<1:
        print("Insira um n�mero final entre 1 e 9")
    if 1<=num2<=9:
        if num2<num1:
            print('Nenhuma tabuada nesse intervalo')
        break
    else:
        num2+=1
for i in range (num1,num2+1,1):
    f1=i*1
    print(i,'x 1 =',f1)
    f2=i*2
    print(i,'x 2 =',f2)
    f3=i*3
    print(i,'x 3 =',f3)
    f4=i*4
    print(i,'x 4 =',f4)
    f5=i*5
    print(i,'x 5 =',f5)
    f6=i*6
    print(i,'x 6 =',f6)
    f7=i*7
    print(i,'x 7 =',f7)
    f8=i*8
    print(i,'x 8 =',f8)
    f9=i*9
    if i==num2:
        print(i,'x 9 =',f9)
    else:
        print(i,' x 9 = ',f9,'\n',sep='')