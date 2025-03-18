quant=int(input())
pont_min=int(input())
count=0
for i in range (quant):
    primeira_fase=int(input())
    segunda_fase=int(input())
    if primeira_fase + segunda_fase >= pont_min:
         if primeira_fase and segunda_fase != 0:
            count+=1
print(count)