while True:
    lfrase=[]
    frase=input().upper()
    for i in range (len(frase)):
        lfrase.append(frase[i])
    for i in range (len(lfrase)):
        if lfrase[i]=='3':
            lfrase.insert(i,'E')
            lfrase.pop(i+1)
        elif lfrase[i]=='4':
            lfrase.insert(i,'A')
            lfrase.pop(i+1)
        elif lfrase[i]=='1':
            lfrase.insert(i,'I')
            lfrase.pop(i+1)
        elif lfrase[i]=='5':
            lfrase.insert(i,'S')
            lfrase.pop(i+1)
    if lfrase==['F','I','M'] or lfrase==['S','A','I','R']:
        break
    a=''
    for i in range (len(lfrase)):
        a+=lfrase[i]
    print(a)