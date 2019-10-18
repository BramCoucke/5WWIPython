antwoord1 = input('Aan de hendel trekken: ')
antwoord2 = input('man duwen: ')

if antwoord1 == 'ja' and antwoord2 == 'ja':
    uitvoer= 2
elif antwoord1 == 'ja' and antwoord2 == 'nee':
    uitvoer= 1
elif antwoord1 == 'nee' and antwoord2 == 'ja':
    uitvoer= 1
elif antwoord1 == 'nee' and antwoord2 == 'nee':
    uitvoer= 5

print(uitvoer)
