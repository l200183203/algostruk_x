#3b
def jumlahHurufKonsonan(hrf):
    konsonan = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    b = 0
    hasil = 0
    for i in hrf :
        if i in konsonan:
            b += len(i)
        else:
            b += 0
    hasil  = len(hrf),b
    return hasil
