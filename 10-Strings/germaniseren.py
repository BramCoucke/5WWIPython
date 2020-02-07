
def germaniseer(zin):
    nieuwe_zin = zin[0].upper()
    for i in range(1,len(zin)):
        if zin[i-1] == ' ':
            nieuwe_zin += zin[i].upper()
        else:
            nieuwe_zin += zin[i]
    return nieuwe_zin


