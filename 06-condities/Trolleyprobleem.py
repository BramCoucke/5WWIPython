antwoord1 = input('Aan de hendel trekken: ')
antwoord2 = input('man duwen: ')

if antwoord1 == 'ja' and antwoord2 == 'ja':
    uitvoer= 2
elif antwoord1 != antwoord2:
    uitvoer= 1
else:
    uitvoer= 5

print(uitvoer)
