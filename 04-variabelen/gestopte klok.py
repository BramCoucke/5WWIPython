#invoer
h1= int(input('h1: '))
m1= int(input('m1: '))
h2= int(input('h2: '))
m2= int(input('m2: '))
h3= int(input('h3: '))
m3= int(input('m3: '))
h4= int(input('h4: '))
m4= int(input('m4: '))

htt=h4- h1
mtt=m4- h1
hbv=h3-h2
mbv=m3-m2
hrt=int((htt-hbv)/2)
mrt=int((mtt-mbv)/2)
h5=h3+hrt
m5=m3+mrt
#uitvoer
print(h5)
print(m5)
