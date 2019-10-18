getal = int(input('geef getal: '))

if getal < 0 and getal % 2 == 0:
    uitvoer = 'neg en even getal'
elif getal < 0 and getal % 2 != 0:
    uitvoer = 'neg en oneven getal'
elif getal > 0 and getal % 2 ==0:
    uitvoer = 'pos en even getal'
elif getal > 0 and getal % 2 != 0:
    uitvoer = 'pos en oneven getal'
else:
    uitvoer = ' gelijk aan nul'

print(uitvoer)
