dobbelsteen1 = int(input('aantal ogen: '))
ds2 = int(input('aantal ogen: '))
ds3 = int(input('aantal ogen: '))
ds4 = int(input('aantal ogen: '))
ds5 = int(input('aantal ogen: '))

max_a = max(dobbelsteen1, ds2, ds3)
min_a = min(dobbelsteen1, ds2, ds3)
mid_a = dobbelsteen1 + ds3 + ds2 - min_a - max_a
max_v = max(ds4, ds5)
min_v = min(ds4, ds5)

if max_a > max_v and mid_a > min_v:
    antwoord = 'aanvaller verliest 0 legers, verdediger verliest 2 legers'
elif min_v >= mid_a and max_v >= max_a:
    antwoord = 'aanvaller verliest 2 legers, verdediger verliest 0 legers'
else:
    antwoord = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'

print(antwoord)
