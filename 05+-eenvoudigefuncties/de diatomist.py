#invoer
straal_kleinecirkel = float(input('r: '))
straal_grotecirkel = float(input('R: '))
from math import floor, pi

n = floor(0.83*(pow(straal_grotecirkel, 2)/ pow(straal_kleinecirkel,2)) -1.9)


bedekkingsgraad = ((n * pow(straal_kleinecirkel,2)*pi) /(pow(straal_grotecirkel,2) *pi))*100

uitvoer = '{} kleine cirkels bedekken {:.2f}% van de grote cirkel'

print(uitvoer.format(n, bedekkingsgraad))
