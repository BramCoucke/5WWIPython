#invoer
sol= int(input('sol: '))

sh=24
sm=39
ss=35.244
sts=(sh*3600)+(sm*60)+ss

sta=sts*sol
tsa=sta%60
mta=sta//60
tma=mta%60
hta=mta//60
tha=hta%24
dta=hta//24
print(sol,'sol =', int(dta),' dagen,', int(tha),' uren,', int(tma),'minuten en', int(tsa),'seconden')


