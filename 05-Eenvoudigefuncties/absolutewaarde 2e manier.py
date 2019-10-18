#13.5100201969301
# 42.06826283274985

#invoer
x = float(input('x: '))
y = float(input('y: '))


uitvoer_ll = abs(abs(x)- abs(y))
uitvoer_rl = abs(x-y)

uitvoer = '{:.4f} \N{LESS-THAN OR EQUAL TO} {:.4f}'


print(uitvoer.format(uitvoer_ll, uitvoer_rl))
