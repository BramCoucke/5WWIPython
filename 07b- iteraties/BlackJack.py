getal = int(input('geef getal: '))
som = 0

while som == 21 or (som<21 and getal == 0) or som > 21:
    som += getal
    getal = int(input('geef getal: '))

if som > 21:
    antwoord = 'Verbrand ({:d})'
elif som == 21:
    print('Gewonnen!')
else:
    antwoord = 'Voorzichtig gespeeld ({:d})'

print(antwoord.format(som))




