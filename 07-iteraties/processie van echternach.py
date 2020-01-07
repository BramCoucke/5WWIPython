aantal_seconden = int(input('aantal seconden:'))
stappen_voorwaarts = 0
stappen_achterwaarts = 0
vorige_voorwaarts =0
vorige_achterwaarts =0

from math import ceil

for i in range(0,aantal_seconden,2):
        stappen_voorwaarts +=2
        vorige_voorwaarts +=stappen_voorwaarts
        stappen_achterwaarts += 1
        vorige_achterwaarts += stappen_achterwaarts


if aantal_seconden % 2 == 0:
    antwoord = vorige_voorwaarts - vorige_achterwaarts
else:
    antwoord = vorige_voorwaarts - vorige_achterwaarts + ceil(aantal_seconden/2)


print(antwoord)
