#invoer
t = float(input('tijd in nanoseconden: '))
c = 299792458
n = 1.000277
d= (c*t*10**-9)/(2*n)
print(d ,'meter')
