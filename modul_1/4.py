#4
def rerata(b):
    hasil = 0
    for i in range (len(b)):
        hasil += b[i]
    hasil = hasil/len(b)
    return hasil
