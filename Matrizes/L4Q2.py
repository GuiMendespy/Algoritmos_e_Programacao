n=int(input())
if n==0:
    print('Vazia')
m1=[]
m2=[]
a=0
for i in range (n**2):
    num1=int(input())
    m1.append(num1)
for i in range (n**2):
    num2=int(input())
    m2.append(num2)
for i in range (n**2):
    a=m1[i]+m2[i]
    print(a)