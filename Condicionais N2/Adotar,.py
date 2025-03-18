ipa=int(input())
if ipa>18:
    adotanteirmaoouascendente=str(input())
    adocao_conjunta=str(input())
    casados_ou_uniaoestavel=str(input())
    ifa=int(input())
    destituido_de_familia=str(input())
    consentimento_dos_pais_conhecidos=str(input())
    consentimento_do_filho_adotivo_maior12=str(input())
    if adotanteirmaoouascendente=="N":
        if adocao_conjunta == "N" or (adocao_conjunta == "S" and casados_ou_uniaoestavel == "S"):
            if ipa-ifa>16:
                if (destituido_de_familia=="N" and consentimento_dos_pais_conhecidos == "S") or destituido_de_familia == "S":
                    if (ifa>=12 and consentimento_do_filho_adotivo_maior12 == "S") or ifa<12:
                        print("Pode adotar")
                    else:
                        print("Nao pode adotar")
                else:
                    print("Nao pode adotar")
            else:
                print("Nao pode adotar")
        else:
            print("Nao pode adotar")
    else:
        print("Nao pode adotar")
else:
  print("Nao pode adotar")