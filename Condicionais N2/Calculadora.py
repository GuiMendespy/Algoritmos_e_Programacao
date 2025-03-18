carne=str(input())
if carne not in ("C", "BF", "BS"):
    print("Op��o inv�lida.")
else:
    se_quer_pao = str(input())
    se_quer_beb_adult = str(input())
    se_quer_bebida_crian = str(input())
    quant_crian = int(input())
    quant_adult = int(input())
    preco_bovino=0.032
    pre�o_frango=0.018
    pre�o_suino=0.015
    pre�o_cerveja=8
    pre�o_refri=6
    if carne=="C":
        carne_bov_adult=200
        carne_fran_adult=100
        carne_suina_adult=100
        carne_bov_crian=200
    if carne=="BF":
        carne_bov_adult=250
        carne_fran_adult=150
        carne_bov_crian=200
    if carne=="BS":
        carne_bov_adult=250
        carne_suina_adult=150
        carne_bov_crian=200
    if se_quer_beb_adult=="S":
        beb_cerv_adult=2
    else:
        beb_cerv_adult=0
    if se_quer_bebida_crian=="S":
        beb_refri_crian=0.5
    else:
        beb_refri_crian=0
    if carne=="C":
       valor_tot=quant_adult*(carne_bov_adult*preco_bovino+carne_fran_adult*pre�o_frango+carne_suina_adult*pre�o_suino)+quant_crian*carne_bov_crian*preco_bovino+beb_cerv_adult*pre�o_cerveja*quant_adult+beb_refri_crian*pre�o_refri*quant_crian
    if carne=="BF":
        valor_tot=quant_adult*(carne_bov_adult*preco_bovino+carne_fran_adult*pre�o_frango)+quant_crian*carne_bov_crian*preco_bovino+beb_cerv_adult*pre�o_cerveja*quant_adult+beb_refri_crian*pre�o_refri*quant_crian
    if carne=="BS":
        valor_tot=quant_adult*(carne_bov_adult*preco_bovino+carne_suina_adult*pre�o_suino)+quant_crian*carne_bov_crian*preco_bovino+beb_cerv_adult*pre�o_cerveja*quant_adult+beb_refri_crian*pre�o_refri*quant_crian
    if se_quer_pao=="N":
        valor_tot *= 0.98
    print("R$: {:.2f}".format(valor_tot))