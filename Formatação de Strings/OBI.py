n=int(input())
frase=list(input())
a=''
frase_i=[]
for i in range(len(frase)):
    frase_i.append(i)
    
for i in range (len(frase)):
    if i==1:
        if frase[i]=='R':
            if frase[i-1]=='U':
                    if frase[i+2]==' ':
                        frase.insert(i+1,'I')
                        frase.pop(i+2)
    if max(frase_i)-1==i:
        if frase[i]=='R':
                if frase[i-1]=='U':
                    if frase[i-2]==' ':
                            frase.insert(i+1,'I')
                            frase.pop(i+2)
    else:
        if frase[i]=='R':
                if frase[i-1]=='U':
                    if frase[i-2]==' ':
                        if frase[i+2]==' ':
                            frase.insert(i+1,'I')
                            frase.pop(i+2)
        
    if i==1:
        if frase[i]=='B':
            if frase[i-1]== 'O':
                if frase[i+2]==' ':
                        frase.insert(i+1,'I')
                        frase.pop(i+2)
    if max(frase_i)-1==i:
        if frase[i]=='B':
            if frase[i-1]== 'O':
                    if frase[i-2]==' ':
                        frase.insert(i+1,'I')
                        frase.pop(i+2)
    else:
        if frase[i]=='B':
            if frase[i-1]== 'O':
                if frase[i+2]==' ':
                    if frase[i-2]==' ':
                        frase.insert(i+1,'I')
                        frase.pop(i+2)
        
for i in range (len(frase)):
    a+=frase[i]
print(a)