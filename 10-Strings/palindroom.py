def is_palindroom(woord):
    omgekeerd_woord =''
    for letter in woord:
        omgekeerd_woord = letter + omgekeerd_woord
    if omgekeerd_woord == woord:
        return(True)
    else:
        return(False)


