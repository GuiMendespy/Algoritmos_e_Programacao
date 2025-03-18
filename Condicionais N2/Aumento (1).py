salant=float(input())
print("{:.2f}".format(salant))
if salant <= 280.00:
    f1 = salant + 0.2 * salant
    f2= (f1-salant)/(salant/100)
    f3= f1-salant
    print(round(f2))
    print("{:.2f}".format(f3))
    print("{:.2f}".format(f1))
if  280.00 < salant < 700.00:
    f11= salant + 0.15 * salant
    f22= (f11-salant)/(salant/100)
    f33= f11 - salant
    print(round(f22))
    print("{:.2f}".format(f33))
    print("{:.2f}".format(f11))
if 700.00 < salant < 1500.00:
    f111= salant + 0.1*salant
    f222= (f111-salant)/(salant/100)
    f333= f111-salant
    print(round(f222))
    print("{:.2f}".format(f333))
    print("{:.2f}".format(f111))
if salant>=1500.00:
    f1111= salant + 0.05*salant
    f2222= (f1111-salant)/(salant/100)
    f3333= f1111-salant
    print(round(f2222))
    print("{:.2f}".format(f3333))
    print("{:.2f}".format (f1111))
