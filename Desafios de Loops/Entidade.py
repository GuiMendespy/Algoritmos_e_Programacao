n = int(input())
altura = 1
cubos_disponiveis = n
while cubos_disponiveis >= altura * (altura + 1) // 2:
    cubos_disponiveis -= altura * (altura + 1) // 2
    altura += 1
altura_maxima = altura - 1
print(altura_maxima)