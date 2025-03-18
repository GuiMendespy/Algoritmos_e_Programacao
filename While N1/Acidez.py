while True:
    entrada = float(input())
    if entrada == -1:
        break  
    if entrada < 7:
        print("ACIDA")
    elif entrada > 7:
        print("BASICA")
    else:
        print("NEUTRA")