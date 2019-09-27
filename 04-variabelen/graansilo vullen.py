#invoer
b= float(input('b: '))
l= float(input('l: '))
c= float(input('c: '))
r= float(input('r: '))
h= float(input('h: '))
p= 3.14

i= r**2*h*p
o=l*b
t_g= (o/10000)*c
t_s= t_g//i+1
l_s= t_g%i
h_s= l_s/(p*r**2)

print(int(t_s))
print(int(h_s))

