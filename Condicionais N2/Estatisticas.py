time=str(input())
if time not in ("GSW", "HOU", "CLE", "BOS"):
    print("Nenhum time de interesse jogando.")
else:
    nomejog=str(input())
    arre_tent_2pts=int(input())
    arre_conv_2pts=int(input())
    arre_tent_3pts=int(input())
    arre_conv_3pts=int(input())
    pts_totais=arre_tent_2pts*2+arre_conv_2pts*2+arre_tent_3pts*3+arre_conv_3pts*3
    if time in ("BOS", "HOU"):
        if pts_totais>30:
            if (arre_tent_2pts*2+ arre_conv_2pts*2)/pts_totais > 50/100 and arre_tent_2pts > 10 or (arre_tent_3pts*3+ arre_conv_3pts*3)/pts_totais >40/100 and arre_tent_3pts > 7:
                print("O time", time,"estah jogando, e", nomejog, "estah indo bem.")
            else:
                print("O time", time, "estah jogando, mas", nomejog, "nao estah indo bem.")
        else:
             print("O time", time,"estah jogando, mas", nomejog, "nao estah indo bem.")
    if time in ("CLE"):
        if pts_totais>30:
            if (arre_tent_2pts*2+ arre_conv_2pts*2)/pts_totais > 50/100 and arre_tent_2pts > 10 and (arre_tent_3pts*3+ arre_conv_3pts*3)/pts_totais >40/100 and arre_tent_3pts > 7:
                print("O time", time,"estah jogando, e", nomejog, "estah indo bem.")
            else:
                print("O time", time, "estah jogando, mas", nomejog, "nao estah indo bem.")
        else:
             print("O time", time,"estah jogando, mas", nomejog, "nao estah indo bem.")
    if time in ("GSW"):
        if pts_totais>30:
            if (arre_tent_2pts*2+ arre_conv_2pts*2)/pts_totais > 50/100 or arre_tent_2pts > 10 or (arre_tent_3pts*3+ arre_conv_3pts*3)/pts_totais >40/100 and arre_tent_3pts > 7:
                print("O time", time,"estah jogando, e", nomejog, "estah indo bem.")
            else:
                print("O time", time, "estah jogando, mas", nomejog, "nao estah indo bem.")
        else:
             print("O time", time,"estah jogando, mas", nomejog, "nao estah indo bem.")
