def dubbels(lijst):
    antwoord = []

    for element in lijst:
        #als element 2keer voorkomt in lijst EN niet in antwoord
        if lijst.count(element) > 1 and element not in antwoord :
            antwoord.append(element)

    return antwoord
