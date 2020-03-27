class MhsTIF:
    def __init__(self, nama, NIM, kota, uang):
        self.nama = nama
        self.NIM = NIM
        self.kota = kota
        self.uang = uang

c0 = MhsTIF("Ika", 10, "Sukoharjo", 240000)
c1 = MhsTIF("Budi", 51, "Sragen", 230000)
c2 = MhsTIF("Ahmad", 2, "Surakarta", 250000)
c3 = MhsTIF("Chandra", 18, "Surakarta", 235000)
c4 = MhsTIF("Eka", 4, "Boyolali", 240000)
c5 = MhsTIF("Fandi", 31, "Salatiga", 250000)
c6 = MhsTIF("Deni", 13, "Klaten", 245000)
c7 = MhsTIF("Galuh", 5, "Wonogiri", 245000)
c8 = MhsTIF("Janto", 23, "Klaten", 245000)
c9 = MhsTIF("Hasan", 64, "Karanganyar", 270000)
c10 = MhsTIF("Khalid", 29, "Purwodadi", 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def urutkanNIM(A):
    baru = {}
    for i in range(len(A)):
        baru[A[i].nama] = A[i].NIM
    listofTuples = sorted(baru.items(), key=lambda x: x[1])
    for elem in listofTuples :
        print(elem[0], ":" , elem[1] )
urutkanNIM(Daftar)
        
