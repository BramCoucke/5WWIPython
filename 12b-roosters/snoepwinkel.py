def bereken_prijs(lijst):
    prijs = 0
    for i in range(len(lijst)):
        tup = lijst[i]
        prijs += tup[1]
    return prijs

def winkelbriefje(lijst):
    resultaat = []
    for i in range(len(lijst)):
        tup = lijst[i]
        resultaat.append(tup[0])
    return resultaat

def sorteer(lijst):
    lijst.sort(key = lambda x: x[1])
    return lijst




tup = lijst[0]
    antwoord = [tup]
    tussenvariabel = tup
    for i in range(1, len(lijst)):
        tup = lijst[i]
        if tup[1] < tussenvariabel[1]:
            antwoord.insert(0,tup)
        else:
            antwoord.append(tup)
    return antwoord
