#8
def apakahTerkandung(a,b):
    x = True
    for i in range(len(b)):
        if a in b:
            x = True
        else:
            x = False
    return x
            
