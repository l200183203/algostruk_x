#13
def katakan(bilangan):
    angka=["","Satu","Dua","Tiga","Empat","Lima","Enam","Tujuh","Delapan",
           "Sembilan","Sepuluh","Sebelas","Duabelas"]
    Hasil = " "
    n = int(bilangan)
    if n >= 0 and n <= 11:
        Hasil = Hasil + angka[n]
    elif n < 20:
        Hasil = katakan(n%10) + " belas"
    elif n < 100:
        Hasil = katakan(n/10) + " puluh" + katakan(n%10)
    elif n < 200:
        Hasil =  " seratus" + katakan(n-100)
    elif n < 1000:
        Hasil = katakan(n/100) + " ratus" + katakan(n%100)
    elif n < 2000:
        Hasil = " seribu" + katakan(n-1000)
    elif n < 10000:
        Hasil = katakan(n/1000) + " ribu" + katakan(n%1000)
    elif n < 20000:
        Hasil = " sepuluh ribu" + katakan(n-10000)
    elif n < 100000:
        Hasil = katakan(n/10000) + " puluh" + katakan(n%10000)
    elif n < 200000:
        Hasil = " seratus" + katakan(n-100000)
    elif n < 1000000:
        Hasil = katakan(n/100000) + " ratus" + katakan(n%100000)
    elif n < 2000000:
        Hasil = " satu juta" + katakan (n-1000000)
    elif n < 10000000:
        Hasil = katakan(n/1000000) + " juta" + katakan(n%1000000)
    elif n < 20000000:
        Hasil = " sepuluh juta" + katakan (n-10000000)
    elif n < 100000000:
        Hasil = katakan(n/10000000) + " puluh" + katakan(n%10000000)
    elif n < 200000000:
        Hasil = " seratus juta" + katakan (n-100000000)
    elif n < 1000000000:
        Hasil = katakan(n/100000000) + " ratus" + katakan(n%100000000)
    elif n == 1000000000:
        Hasil = " satu milyar" + katakan(n%1000000000)
    else:
        Hasil = "Angka hanya sampai satu milyar"
    return Hasil
