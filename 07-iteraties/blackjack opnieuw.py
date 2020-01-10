kaart = int(input('y: '))
som = kaart

while kaart != 0 and som < 21:
    kaart = int(input('y: '))
    som += kaart

print(som)
