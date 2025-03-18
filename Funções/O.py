def maior(j):
    lista=[]
    for i in j:
        lista+= [int(i)]
    return max(lista)
n=input().split(' ')
print(f'{maior(n)} eh o maior')