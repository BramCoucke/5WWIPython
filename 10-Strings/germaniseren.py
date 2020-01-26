#overloop alle letters vd string
# indienletter een spatie is
#volgende letter w hoofdletter
#plak aan nieuwe zin
def germaniseren(zin):
    nieuwe_zin = ''
    for i in range (0,len(zin)):
        if zin[i] == ' ':
            nieuwe_zin += ' '+ zin[i + 1].upper()
        else:
            nieuwe_zin += zin[i]
    return nieuwe_zin


print(germaniseren('dit is een test'))

