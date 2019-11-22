bruto_jaarsalaris = float(input('geef bruto aantal: '))


antwoord1 = '+ bruto jaarsalaris {:>2.2f}'
antwoord2 = '- rsz {:>.2f}'
antwoord3 = '- voorheffing {:>.2f}'
antwoord4 = '+ netto jaarsalaris {:>.2f}'
antwoord5 = '+ netto maandsalaris {:>.2f}'
waarde2 = bruto_jaarsalaris / 100 * 13.07
netto_belastbaar_inkomen = bruto_jaarsalaris - waarde2

if bruto_jaarsalaris <= 13250:
    waarde3 = 0
elif bruto_jaarsalaris <= 23390:
    waarde3 = ((13250-8860)/4)
elif bruto_jaarsalaris <= 40480:
    waarde3 = ((13250-8860)/4) + ((23390-13250)/5*2)
else:
    waarde3 = ((13250-8860)/4) + ((23390-13250)/5*2) + ((40480-23390)/100*45)

waarde4 = netto_belastbaar_inkomen - waarde3
waarde5 = waarde4/12

print(antwoord1.format(bruto_jaarsalaris))
print(antwoord2.format(waarde2))
print(antwoord3.format(waarde3))
print('==============================')
print(antwoord4.format(waarde4))
print(antwoord5.format(waarde5))
