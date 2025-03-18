n=input()
if len(n)==1:
    slinha=[]
    for i in range (int(n)*2):
        linha=input()
        a=linha.split()
        for i in range (len(a)):
            a[i]=int(a[i])
        for i in range (1):
            b=sum(a)
            slinha.append(b)
    j=0
    k=0
    for i in range (int(n)):
        j+=slinha[i]
    for i in range (len(slinha)-1,int((len(slinha)/2)-1),-1):
        k+=slinha[i]
    if k==j:
        print('SIM')
    else:
        print('NAO')
elif len(n)==3:
    a=n.split()
    slinha=[]
    for i in range (len(a)):
                a[i]=int(a[i])
    for i in range (1):
                b=sum(a)
                slinha.append(b)
    for i in range (3):
        n=input()
        a=n.split()
        for i in range (len(a)):
                a[i]=int(a[i])
        for i in range (1):
                b=sum(a)
                slinha.append(b)
    j=0
    k=0
    for i in range (int(len(slinha)/2)):
        j+=slinha[i]
    for i in range (len(slinha)-1,int((len(slinha)/2)-1),-1):
        k+=slinha[i]
    if k==j:
        print('SIM')
    else:
        print('NAO')
else:
    a=n.split()
    slinha=[]
    for i in range (len(a)):
                a[i]=int(a[i])
    for i in range (1):
                b=sum(a)
                slinha.append(b)
    for i in range (5):
        n=input()
        a=n.split()
        for i in range (len(a)):
                a[i]=int(a[i])
        for i in range (1):
                b=sum(a)
                slinha.append(b)
    j=0
    k=0
    for i in range (int(len(slinha)/2)):
        j+=slinha[i]
    for i in range (len(slinha)-1,int((len(slinha)/2)-1),-1):
        k+=slinha[i]
    if k==j:
        print('SIM')
    else:
        print('NAO')