def ontdubbelen(woord):
    nieuw_woord = woord[0]
    for i in range(len(woord)-1):
        if woord[i] == woord[i+1]:
            nieuw_woord = nieuw_woord
        else:
            nieuw_woord += woord[i+1]
    return(nieuw_woord)



