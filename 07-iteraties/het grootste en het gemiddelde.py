#invoer
aantal_getallen = int(input('aantal getallen: '))
getal1 = int(input('geefgetal: '))
maximum = getal1
som = getal1

for getal in range(0, aantal_getallen - 1):
    getal = int(input('geef getal: '))
    som = som + getal
    maximum = max(maximum, getal)
    gem = som/aantal_getallen


print('Het grootste getal is',maximum,'en het gemiddelde is {:.2f}'.format(gem))

