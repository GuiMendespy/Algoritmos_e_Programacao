psnr=int(input())
enq=str(input())
exp=str(input())
if 80 < psnr <= 90:
        if enq in ("bom", "excelente") and exp == "bem exposta":
            print("para imprimir")
elif 80 <= psnr < 90:
    if enq in ("bom", "excelente"):
        print("boa")
    else:
        print("marromeno")
elif 50 <= psnr <= 80:
        if enq == "excelente" and exp == "bem exposta":
            print("boa")
        else:
            print("marromeno")
else:
        if enq == "excelente" and exp == "bem exposta":
            print("marromeno")
        else:
            print("lixo")