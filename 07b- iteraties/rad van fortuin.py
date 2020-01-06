woord = str(input('verborgen woord: '))
gedraaide_geldbedrag = int(input('bedrag: '))
letter = input('letter: ')
gegokte_letters = ''
geldsom = 0
while letter in woord and not letter in gegokte_letters:
    gegokte_letters += letter
    geldsom += gedraaide_geldbedrag
    letter = input('letter: ')

print(geldsom)
