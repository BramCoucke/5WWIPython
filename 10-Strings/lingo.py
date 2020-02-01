def hint(gok, oplossing):

    hint = ''
    for i in range(len(gok)):
        if oplossing.find(gok[i]) != -1:
            if gok[i] == oplossing[i]:
                hint += gok[i].upper()
            else:
                hint += gok[i]
        else:
            hint += '.'
    return hint

