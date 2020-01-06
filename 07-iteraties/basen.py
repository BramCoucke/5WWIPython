aantal_basen = int(input('aantal basen: '))
verschil = 0
woord =''
uitkomst_soorten =''

for i in range(aantal_basen):
    voorgaande = woord
    soort = str(input('soort: '))
    woord = voorgaande + soort

if 'A' in woord:
    verschil += 1
    uitkomst_soorten += 'A'
else:
    verschil +=0
if 'C' in woord:
    verschil += 1
    uitkomst_soorten += ' C'
else:
    verschil +=0
if 'G' in woord:
    verschil += 1
    uitkomst_soorten += ' G'
else:
    verschil +=0
if 'T' in woord:
    verschil += 1
    uitkomst_soorten += ' T'
else:
    verschil +=0

if verschil == 1:
    antwoord = 'De DNA-keting bevat {:d} soort base:'
else:
    antwoord = 'De DNA-keting bevat {:d} verschillende soorten basen:'

print(antwoord.format(verschil),uitkomst_soorten)
