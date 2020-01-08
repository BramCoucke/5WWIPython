verborgen_woord = str(input('geef woord: '))
gedraaide_bedrag = int(input('geef berdag: '))
geg_letter = str(input('geef letter: '))
bedrag = 0
gegokte_letters =''

while geg_letter in verborgen_woord and not geg_letter in gegokte_letters:
    gegokte_letters += geg_letter
    bedrag += gedraaide_bedrag
    geg_letter = str(input('geef letter: '))

print(bedrag)
