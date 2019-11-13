x1 = float(input('geef getal: '))
x2 = float(input('geef getal: '))
x3 = float(input('geef getal: '))
x4 = float(input('geef getal: '))

maxi = max(x1,x2,x3,x4)
mini = min(x1,x2,x3,x4)

mid_1 = max(min(x1,x2),min(x2,x3),min(x2,x3))
mid_2 = x1+x2+x3+x4 - mini -maxi -mid_1

print(mid_1)
print(mid_2)
