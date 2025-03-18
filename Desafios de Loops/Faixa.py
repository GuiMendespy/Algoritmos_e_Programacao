n=1
while n!=0:
    idade=int(input())
    if idade==0:
        break
    if idade<0:
        print("Voc� ainda n�o nasceu.")
    elif 1<=idade<=11:
        print("Voc� � uma crian�a.")
    elif 12<=idade<=17:
        print("Voc� � um adolescente.")
    elif 18<= idade <=35:
        print("Voc� � um jovem.")
    elif 36<=idade<=64:
        print("Voc� � um adulto.")
    elif idade>=65:
        print("Voc� � um idoso.")