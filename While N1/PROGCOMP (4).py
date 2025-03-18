num_maior = None
while True:
    valor = int(input())
    if valor == 0:
        break  
    else:
        if num_maior is None or valor > num_maior:
            num_maior = valor
if num_maior is not None:
    print(num_maior)