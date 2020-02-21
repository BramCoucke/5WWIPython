
antwoord = []
kleur = input('geef woord: ')
while kleur != 'STOP':
    if kleur != '?':
        antwoord.append(kleur)
    elif len(antwoord) > 0:
        print(antwoord.pop(0))
    kleur = input('geef volgend kleur: ')


