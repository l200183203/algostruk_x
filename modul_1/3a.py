#3a
def jumlahHurufVokal(hrf):
    vokal = 'aiueoAIUEO'
    a = 0
    hasil = 0
    for i in hrf :
        if i in vokal:
            a += len(i)
        else:
            a += 0
    hasil  = len(hrf),a
    return hasil
