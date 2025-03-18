count4=0
count5=0
count9=0
while True:
    num=int(input())
    if num==4:
        count4+=1
    elif num==5:
        count5+=1
    elif num==9:
        count9+=1
    elif num==0:
        break
if count4>count5>count9:
    print('canal 4:',count4)
    print('canal 5:',count5)
    print('canal 9:',count9)
elif count4>count9>count5:
    print('canal 4:',count4)
    print('canal 9:',count9)
    print('canal 5:',count5)
elif count5>count4>count9:
    print('canal 5:',count5)
    print('canal 4:',count4)
    print('canal 9:',count9)
elif count5>count9>count4:
    print('canal 5:',count5)
    print('canal 9:',count9)
    print('canal 4:',count4)
elif count9>count4>count5:
    print('canal 9:',count9)
    print('canal 4:',count4)
    print('canal 5:',count5)
elif count9>count5>count4:
    print('canal 9:',count9)
    print('canal 5:',count5)
    print('canal 4:',count4)
elif count4==count5==count9:
    print('canal 9:',count9)
    print('canal 5:',count5)
    print('canal 4:',count4)
elif count4==count5<count9:
    print('canal 9:',count9)
    print('canal 5:',count5)
    print('canal 4:',count4)
elif count4==count5>count9:
    print('canal 5:',count5)
    print('canal 4:',count4)
    print('canal 9:',count9)
elif count4>count5==count9:
    print('canal 4:',count4)
    print('canal 9:',count9)
    print('canal 5:',count5)
elif count4<count5==count9:
    print('canal 9:',count9)
    print('canal 5:',count5)
    print('canal 4:',count4)
elif count5>count4==count9:
    print('canal 5:',count5)
    print('canal 9:',count9)
    print('canal 4:',count4)
elif count5<count4==count9:
    print('canal 9:',count9)
    print('canal 4:',count4)
    print('canal 5:',count5)