def versleutel_woord(oud_woord, aantal_plaatsen):
    nieuw_woord = ''
    for i in range(len(oud_woord)):
        tussen_letter =''
        if oud_woord[i] == ' ':
            nieuw_woord += '@'
        elif ord('a') <= ord(oud_woord[i]) <= ord('z'):
            tussen_letter += oud_woord[i].upper()
            nieuw_woord += chr(ord(tussen_letter) + aantal_plaatsen)
        else:
            nieuw_woord += chr(ord(oud_woord[i]) + aantal_plaatsen)
    nieuw_woord.replace('@',' ')
    return nieuw_woord

def versleutel_zin(bericht, plaatsen):
    nieuw_woord = ''
    for i in range(len(bericht)):
        tussen_letter =''
        if bericht[i] == ' ':
            nieuw_woord += '@'
        elif ord('a') <= ord(bericht[i]) <= ord('z'):
            tussen_letter += bericht[i].upper()
            nieuw_woord += chr(ord(tussen_letter) + plaatsen)
        else:
            nieuw_woord += chr(ord(bericht[i]) + plaatsen)
    nieuw_woord.replace('@',' ')
    return nieuw_woord



