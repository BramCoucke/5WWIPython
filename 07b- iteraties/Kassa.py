getal = float(input('geef getal: '))
som = 0
while getal != 0:
    som += getal
    getal = float(input('geef getal: '))

print('De totale prijs is € {:.2f}'.format(som))
