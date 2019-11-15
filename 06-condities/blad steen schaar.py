gebaar_speler_1 = str(input('blad, steen of schaar: '))
gebaar_speler_2 = str(input('blad, steen of schaar: '))

if gebaar_speler_1 == gebaar_speler_2:
    antwoord = 'onbeslist'
elif (gebaar_speler_1 == 'steen' and gebaar_speler_2 == 'blad')or(gebaar_speler_1 == 'blad' and gebaar_speler_2 == 'schaar')or(gebaar_speler_1== 'schaar' and gebaar_speler_2== 'steen'):
    antwoord = 'speler 2 wint'
else:
    antwoord = 'speler 1 wint'

print(antwoord)

