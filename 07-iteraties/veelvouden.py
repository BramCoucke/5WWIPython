getal = int(input('geef getal: '))
som = 0

for i in range(0, 101,):
    if i * getal > 100:
        som = som + 0
    else:
        som = som + i * getal

print(som)




