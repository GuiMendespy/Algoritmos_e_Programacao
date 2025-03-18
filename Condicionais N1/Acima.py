n1=float(input())
n2=float(input())
n3=float(input())
m=(n1+n2+n3)/3
count=0
if n1>m:
    count+=1
if n2>m:
    count+=1
if n3>m:
    count+=1
print(count)