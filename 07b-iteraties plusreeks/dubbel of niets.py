totaal_kapitaal = int(input('geef kapitaal: '))
startkapitaal = input('startkapitaal: ')
gekozen_kleur = str(input('geef kleur: '))
gedraaid_kleur =str(input('gedraaid kleur: '))
niets =1


if startkapitaal =='alles':
    uiteindelijk_startbedrag = totaal_kapitaal
else:
    uiteindelijk_startbedrag = startkapitaal

while gekozen_kleur != 'stop' and uiteindelijk_startbedrag < totaal_kapitaal:
    if gedraaid_kleur == gekozen_kleur:
        uiteindelijk_startbedrag = uiteindelijk_startbedrag * 2
    else:
        uiteindelijk_startbedrag = 0
    totaal_kapitaal = totaal_kapitaal + uiteindelijk_startbedrag
    gekozen_kleur = str(input('gekozenkleur: '))
    if gekozen_kleur == 'stop':
        niets=1
    else:
        gedraaid_kleur = str(input('gerdaaidkleur'))


print(totaal_kapitaal)





