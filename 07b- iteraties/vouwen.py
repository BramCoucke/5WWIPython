dikte_papier = int(input('geef dikte: '))
afstand_hemellichaam = int(input('geef afstand: '))
vouwen = 0

while dikte_papier < afstand_hemellichaam:
    dikte_papier = dikte_papier*2
    vouwen += 1

antwoord = 'Na {:d} keer vouwen bedraagt de dikte van het papier {:d} mm.'
print(antwoord.format(vouwen,dikte_papier))

