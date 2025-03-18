crime_delator=str(input())
if crime_delator!="roubo" and crime_delator!= "tr�fico" and crime_delator!= "homic�dio":
    print("Crime inv�lido.")
else:
    if crime_delator=="roubo" or crime_delator=="tr�fico":
        valor_delator=int(input())
    crime_delatado=input()
    if crime_delatado=="roubo" or crime_delatado=="tr�fico":
        valor_dalatado=int(input())
    if crime_delator!="roubo" and crime_delator!= "tr�fico" and crime_delator!= "homic�dio" or crime_delatado!="roubo" and crime_delatado!= "tr�fico" and crime_delatado!= "homic�dio":
        print("Crime inv�lido.")
    elif (crime_delator=="roubo" or crime_delator=="tr�fico") and crime_delatado=="homic�dio":
        print("Dela��o concedida.")
    elif crime_delator=="roubo" and crime_delatado=="roubo" and valor_dalatado>(5*valor_delator):
        print("Dela��o concedida.")
    elif crime_delator=="roubo" and crime_delatado=="tr�fico"and valor_dalatado>(3*valor_delator):
        print("Dela��o concedida.")
    elif crime_delator=="tr�fico" and crime_delatado=="tr�fico" and valor_dalatado>(5*valor_delator):
        print("Dela��o concedida.")
    elif crime_delator=="homic�dio" and crime_delatado=="homic�dio":
        print("Dela��o concedida.")
    else:
        print("Dela��o rejeitada.")