nde_getal = int(input('geef het hoeveelste getal: '))
som=1
voorgaande = 0
for i in range(1, nde_getal):
    som += voorgaande
    voorgaande = som - voorgaande
print(som)




