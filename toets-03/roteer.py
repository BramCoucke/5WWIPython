def roteer(woord, start_plaats):
    nieuw_woord =''
    for letter in woord:
        plaats = woord.find(letter) + start_plaats
        if plaats >len(woord) - 1:
            while plaats >= len(woord):
                plaats -= len(woord)

        nieuw_woord += woord[plaats]
    return nieuw_woord


