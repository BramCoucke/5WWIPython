def yiq(kleur):
    y = 0.299 * kleur[0] + 0.587 * kleur[1] + 0.114 * kleur[2]
    i = kleur[0] * 0.596 + kleur[1] * (-0.274) + kleur[2] * (-0.322)
    q = kleur[0] * 0.211 + kleur[1] * (-0.523) + kleur[2] * 0.312
    return(y, i, q)

