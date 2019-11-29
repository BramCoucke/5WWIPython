from random import randint

munt = 0
aantal_experimenten = 10000

for i in range(aantal_experimenten):
    munt += randint(0, 1)

print(munt , aantal_experimenten-munt)
# op einde van whilelus NIEUWE INVOER vragen
