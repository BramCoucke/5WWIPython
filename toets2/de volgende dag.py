vorige_dag = int(input('geef dag: '))
maand_opgave = int(input('geef maand: '))
jaar_opgave = int(input('geef jaar: '))
if maand_opgave == 2 and vorige_dag == 28 and jaar_opgave % 400 == 0:
    antwoord1 = 29
    antwoord2 = 2
    antwoord3 = jaar_opgave
elif maand_opgave == 2 and vorige_dag == 28 and jaar_opgave % 100 == 0:
    antwoord1 = 1
    antwoord2 = 3
    antwoord3 = jaar_opgave
elif maand_opgave == 2 and vorige_dag == 29 and jaar_opgave % 4 == 0 :
    antwoord1 = 1
    antwoord2 = 3
    antwoord3 = jaar_opgave
elif maand_opgave == 2 and vorige_dag == 28 and jaar_opgave % 4 != 0:
    antwoord1 = 1
    antwoord2 = 3
    antwoord3 = jaar_opgave
elif maand_opgave == 12 and vorige_dag == 31:
    antwoord1 = 1
    antwoord2 = 1
    antwoord3 = jaar_opgave + 1
elif maand_opgave == 12 and vorige_dag == 30:
    antwoord1 = 31
    antwoord2 = maand_opgave
    antwoord3 = jaar_opgave
elif vorige_dag == 31:
    antwoord1 = 1
    antwoord2 = maand_opgave + 1
    antwoord3 = jaar_opgave
elif vorige_dag == 30 and maand_opgave != 1 and maand_opgave != 3 and maand_opgave != 5 and maand_opgave != 7 and maand_opgave != 8 and maand_opgave != 10:
    antwoord1 = 1
    antwoord2 = maand_opgave + 1
    antwoord3 = jaar_opgave
else:
    antwoord1 = vorige_dag + 1
    antwoord2 = maand_opgave
    antwoord3 = jaar_opgave

print('{}/{}/{}'.format(antwoord1,antwoord2,antwoord3))
