getal = int(input('geef getal: '))
deler = 0
getal_1 = getal
from math import floor

while getal_1 >= 1:
    term = getal_1 % 10
    deler += term
    getal_1 =  floor(getal_1 / 10)

if getal % deler == 0:
    antwoord = '{:d} is een Harshadgetal'
else:
    antwoord = '{:d} is geen Harshadgetal'

print(antwoord.format(getal))
