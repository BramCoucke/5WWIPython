getal = int(input('geef getal: '))
max = getal

aantal = 0

while getal > 0:
    if getal >= max:
        max = getal
    else:
        max = max
    aantal += 1
    getal = int(input('geef getal: '))

t = ((aantal+1)*max)/aantal -1
antwoord ='Het aantal geproduceerde tanks wordt geschat op {:d}.'

print(antwoord.format(t))
