#14
def formatRupiah(bilangan):
    y = str(bilangan)
    if len(y) <= 3 :
        return 'Rp ' + y
    else:
        p = y[-3:]
        q = y[:-3]
        return formatRupiah(q) + '.' + p
        print ('Rp ' + formatRupiah(q) + '.' + p)
