snelheid_stijn = int(input('snelheid stijn in m/s: '))
snelheid_kaat =  int(input('snelheid kaat in m/s: '))
afstand = int(input('geef afstand: '))
afgelegde_afstand_s= 0
afgelegde_afstand_k= 0
aantal_seconden = 0

while afstand > afgelegde_afstand_s + afgelegde_afstand_k:
    aantal_seconden += 1
    afgelegde_afstand_s = aantal_seconden * snelheid_stijn
    afgelegde_afstand_k = aantal_seconden * snelheid_kaat

antwoord ='Na {:d} s hebben Stijn en Kaat elkaar ontmoet.'

print(antwoord.format(aantal_seconden))

