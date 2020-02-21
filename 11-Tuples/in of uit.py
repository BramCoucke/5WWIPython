def binnen_of_buiten(middelpunt, punt_cirkel, random_punt):
    from math import sqrt
    straal = sqrt((punt_cirkel[0] - middelpunt[0])**2 + (punt_cirkel[1] - middelpunt)**2)
    afstand_tot_middelpunt = sqrt((random_punt[0] - middelpunt[0])**2 + (random_punt[1] - middelpunt)**2)

    if afstand_tot_middelpunt > straal:
        plaats = 'buiten'
    elif afstand_tot_middelpunt < straal:
        plaats = 'binnen'
    else:
        plaats = 'op'

    return plaats, round(afstand_tot_middelpunt, 4)


