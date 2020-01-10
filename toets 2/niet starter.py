getal = float(input('geef getal: '))
aantal_stappen = 1
optelling = 0.5
term = optelling

while optelling < getal:
    aantal_stappen +=1
    optelling += term/2
    term = term / 2


print(aantal_stappen, optelling)
