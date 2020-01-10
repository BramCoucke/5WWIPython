getal_1 = int(input('geef eerste getal: '))
getal_2 = int(input('geef tweede getal: '))
som_1 = 0
som_2 = 0
deler_1 = 1
deler_2 = 1

for i in range(1,getal_1):
    if getal_1 % deler_1 == 0:
        som_1 += deler_1
    else:
        som_1 = som_1
    deler_1 += 1

for i in range(1,getal_2):
    if getal_2 % deler_2 == 0:
        som_2 += deler_2
    else:
        som_2 = som_2
    deler_2 += 1
if som_1 == getal_2 and som_2 == getal_1:
    antwoord = '{:d} en {:d} zijn bevriende getallen'
else:
    antwoord = '{:d} en {:d} zijn geen bevriende getallen'

print(antwoord.format(getal_1, getal_2))
