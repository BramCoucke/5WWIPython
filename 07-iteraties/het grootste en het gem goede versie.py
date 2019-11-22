aantal = int(input('aantal getallen: '))
getal_0 = int(input('geef getal: '))
som = getal_0
grootste = getal_0

for i in range(aantal - 1):
    getal = int(input('geef getal:'))
    som += getal
    grootste = max(grootste, getal)

gemiddelde = som / aantal

print(gemiddelde, grootste)
