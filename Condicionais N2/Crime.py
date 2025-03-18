p1=str(input())
p2=str(input())
p3=str(input())
p4=str(input())
p5=str(input())
cont_true=0
if p1=="True":
    cont_true +=1
if p2=="True":
    cont_true +=1
if p3=="True":
    cont_true +=1
if p4=="True":
    cont_true +=1
if p5=="True":
    cont_true +=1

if  cont_true== 5 :
    print("Telefonou para a vitima?")
    print("Esteve no local do crime?")
    print("Mora perto da vitima?")
    print("Devia para a vitima?")
    print("Ja trabalhou com a vitima?")
    print("Assassino")
elif cont_true==0 or cont_true==1:
    print("Telefonou para a vitima?")
    print("Esteve no local do crime?")
    print("Mora perto da vitima?")
    print("Devia para a vitima?")
    print("Ja trabalhou com a vitima?")
    print("Inocente")
elif  cont_true==2:
    print("Telefonou para a vitima?")
    print("Esteve no local do crime?")
    print("Mora perto da vitima?")
    print("Devia para a vitima?")
    print("Ja trabalhou com a vitima?")
    print("Suspeita")
else:
    print("Telefonou para a vitima?")
    print("Esteve no local do crime?")
    print("Mora perto da vitima?")
    print("Devia para a vitima?")
    print("Ja trabalhou com a vitima?")
    print("Cumplice")