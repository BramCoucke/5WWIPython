kleur1 = str(input('kleur hoed 1: '))
kleur2 = str(input('kleur hoed 2: '))
welke_persoon_omgekeerde = str(input('1 of 2: '))

if kleur1 == kleur2 and kleur1== 'zwart' and welke_persoon_omgekeerde == 2 or kleur1 == kleur2 and kleur1 == 'wit' and welke_persoon_omgekeerde == 1:
    antwoorda = 'zwart'
    antwoord2 = 'wit'
elif kleur1 == kleur2 and kleur1 == 'wit' and welke_persoon_omgekeerde == 2 or kleur1 == kleur2 and kleur1== 'zwart' and welke_persoon_omgekeerde == 1:
    antwoorda = 'wit'
    antwoord2 = 'zwart'
elif kleur1 == 'zwart' and welke_persoon_omgekeerde == 1 or kleur2 == 'wit' and welke_persoon_omgekeerde == 2:
    antwoorda = 'zwart'
    antwoord2 = 'zwart'
else:
    antwoorda = 'wit'
    antwoord2 = 'wit'

print(antwoorda)
print(antwoord2)



