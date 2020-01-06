getal = int(input('geef getal: '))
deler = 2

while (getal % deler) != 0 and deler < getal:
    deler += 1

if deler == getal:
    antwoord = '{:d} is een priemgetal'
else:
    antwoord = '{:d} is geen priemgetal'

print(antwoord.format(getal))
