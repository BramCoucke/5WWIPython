#invoer
k = 8.99 * 10**9
q_1 = 2.0 *10**-6
q_2 = 1.0 *10**-6
r = float(input('geef straal: '))
r = r*10**-2
#berekening
f = k * q_1 *q_2 /r**2
#uitvoer
print(f)
