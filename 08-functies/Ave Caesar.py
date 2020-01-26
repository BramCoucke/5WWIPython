def is_letter(t):
    return ord('A') <= ord(t) <= ord('z')


def roteer(letter ,plaatsen):
    #volgnummer in het alfabet bepaald van de gegeven letter
    volgnummer_letter = min(ord(letter) % ord('a'), ord(letter) % ord('A'))
    # volgnummer in alfabet van nieuwe letter
    nieuw_volgnummer = (volgnummer_letter + plaatsen) % 26
    # offset
    offset = nieuw_volgnummer - volgnummer_letter
    return chr(ord(letter) + offset)


def versleutel(woord, n):
    rotatie =''





