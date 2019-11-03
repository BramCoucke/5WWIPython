wind_snelheid = int(input('snelheid: '))

if wind_snelheid >= 250:
    uitvoer = 'categorie 5'
elif wind_snelheid >= 210:
    uitvoer = 'categorie 4'
elif wind_snelheid >= 178:
    uitvoer = 'categorie 3'
elif wind_snelheid >= 154:
    uitvoer = 'categorie 2'
elif wind_snelheid >= 119:
    uitvoer = 'categorie 1'
else:
    uitvoer = 'geen orkaan'

print(uitvoer)
