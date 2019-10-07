
#invoer
t = float(input('t: '))
w = float(input('w: '))
w_inmeterpsec = w/3.6

uitvoer = 13.12 + 0.6215 * t + (0.3965 * t - 11.37) * pow((3.6 * w_inmeterpsec) , 0.16)

print(uitvoer)
