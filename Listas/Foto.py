lista=[]
for i in range (4):
     num=float(input())
     lista.append(num)
     lista.sort()
print('{:.2f}'.format(min(lista)))
print('{:.2f}'.format(lista[2]))
print('{:.2f}'.format(max(lista)))
print('{:.2f}'.format(lista[1]))