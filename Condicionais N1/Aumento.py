sali=float(input())
if sali>500:
    salf1=(sali+10*sali/100)
    print("{:.2f}".format(salf1))
if (sali>300) and (sali<500):
    salf2=(sali+7*sali/100)
    print("{:.2f}".format(salf2))
if sali<300:
    salf3=(sali+5*sali/100)
    print("{:.2f}".format(salf3))