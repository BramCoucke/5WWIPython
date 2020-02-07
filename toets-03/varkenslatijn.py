def verwijder_medeklinkers(woord):
    if woord[0] == 'a' or woord[0] =='e' or woord[0] =='u'or woord[0] =='i'or woord[0] =='o':
        return(woord)
    else:



        return(woord)

def varkenslatijn(woord):
    verwijder_medeklinkers(woord)
    if woord[len(woord)] =='a' or woord[len(woord)] == 'u' or woord[len(woord)] == 'i':
        woord +='nt'
    else:
        woord +='ibus'
    return(woord)


def vertaal(zin):

