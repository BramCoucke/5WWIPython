#invoer
a = int(input('a: '))
b = int(input('b: '))

oefening_1 = '{:>6d} + {:<6d} ='


print(oefening_1.format(a, b),a+b)


print(oefening_1.format(a*10, b*10),a*10+ b*10)

print(oefening_1.format(a*pow(10,2), b*pow(10,2)),a*pow(10,2)+ b * pow(10,2))

print(oefening_1.format(a*pow(10,3), b*pow(10,3)),a*pow(10,3)+ b * pow(10,3))

print(oefening_1.format(a*pow(10,4), b*pow(10,4)),a*pow(10,4)+ b * pow(10,4))
