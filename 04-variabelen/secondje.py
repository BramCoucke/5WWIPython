#invoer
tts=int(input('tts:'))

stt=tts%60
mtt=tts//60
ttm=mtt%60
htt=mtt//60
tth=htt%24
ttd=htt//24

print(ttd,'d',tth,':',ttm,':',stt)
