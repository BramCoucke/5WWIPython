def hoogtemeters(lijst):
    res = []

    for i in range(len(lijst) - 1):
            res.append(lijst[i+1] - lijst[i] )
    return(res)

def dalen_en_stijgen(lijst):
    stijgend = 0
    dalend = 0
    for i in range(len(lijst)):
        if lijst[i] > 0:
            stijgend += lijst[i]
        else:
            dalend -= lijst[i]
    return(dalend,stijgend)

