#invoer
score_thuisploeg = float(input('geef score thuisploeg:'))
score_uitploeg = float(input('geef score uitploeg:'))

if score_thuisploeg >= 20 + score_uitploeg:
    uitvoer1 = ('thuisploeg: 730.00')
    uitvoer2 = ('uitploeg: 270.00')
elif score_thuisploeg >= 10 + score_uitploeg:
    uitvoer1 = ('thuisploeg: 630.00')
    uitvoer2 = ('uitploeg: 370.00')
elif score_thuisploeg > score_uitploeg:
    uitvoer1 = ('thuisploeg: 530.00')
    uitvoer2 = ('uitploeg: 470.00')
elif score_thuisploeg + 20 <= score_uitploeg:
    uitvoer1 = ('thuisploeg: 130.00')
    uitvoer2 = ('uitploeg: 870.00')
elif score_thuisploeg + 10 <= score_uitploeg:
    uitvoer1 = ('thuisploeg: 230.00')
    uitvoer2 = ('uitploeg: 770.00')
elif score_thuisploeg < score_uitploeg:
    uitvoer1 = ('thuisploeg: 330.00')
    uitvoer2 = ('uitploeg: 670.00')

print(uitvoer1)
print(uitvoer2)
