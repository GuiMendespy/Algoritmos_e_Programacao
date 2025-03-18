r1=int(input())
r2=int(input())
r3=int(input())

if (r2-r3) < r1 < r2 + r3 and (r1 - r2) < r3 < r1 + r2 and (r1 - r3) < r2 < r1 + r3:
  if r1!=r2!=r3!=r1:
      print("escaleno")

  elif (r1==r2 and r1!=r3) or (r3 == r1 and r3!=r2) or r2==r3 and r1!=r2:
      print("isoceles")
  elif r1==r2 and r2==r3:
      print("equilatero")

else:
    print("impossivel")
  