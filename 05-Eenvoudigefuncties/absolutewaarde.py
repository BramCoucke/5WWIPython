#
#13.5100201969301
# 42.06826283274985

#invoer
x = float(input('x: '))
y = float(input('y: '))

uitvoer_ll = abs(abs(x)-abs(y))
uitvoer_rl = abs(x-y)

print( round( uitvoer_ll,4),'\N{LESS-THAN OR EQUAL TO}', round(uitvoer_rl, 4))
