getal = int(input('geef getal: '))
som = getal
while som < 21 and getal !=0 :
    getal = int(input('geef getal: '))
    som += getal

if som > 21:
    antwoord = 'Verbrand ({:d})'
elif som == 21:
    antwoord = 'Gewonnen!'
else:
    antwoord = 'Voorzichtig gespeeld ({:d})'

if som != 21:
    print(antwoord.format(som))
else:
    print(antwoord)




