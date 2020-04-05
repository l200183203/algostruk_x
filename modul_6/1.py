class MhsTIF:
    def __init__(self, nama, nim, kota, uang):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uang = uang
    def __str__ (self) :
        s = self.nama + " " + str(self.nim) + " " + self.kota + " " + str(self.uang)
        return s
    def getNim(self) :
        return self.nim

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

daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def mergesort(A): #untuk menghitung mergeshort
    
    if len(A) > 1:
        mid = len(A) // 2 #membelah list
        kiri = A[:mid] #membelah ke kiri
        kanan = A[mid:] #membelah ke kanan

        mergesort(kiri) #memanggil lebih lanjut mergeshort
        mergesort(kanan) #untuk separuh kiri dan separuh kanan

        i = 0 ; j = 0 ; k = 0
        while i < len (kiri) and j < len (kanan): #while lope ini
            if kiri[i].getNim() < kanan[j].getNim(): #jika loop ini
                A[k] = kiri[i] #menggabungkan kedua list 
                i = i +1 #separuh kiri dan separuh kanan
            else:
                A[k] = kanan[j] #a samadengan kanan
                j = j +1 #maka kanan di tambah 1
            k = k+1 #dua list urut

        while i < len(kiri): #ketika i lebih kecil dari len kiri
            A[k]= kiri [i] #maka a samadengan kiri
            i= i+1 #kiri samadengan ditambah 1
            k = k +1 #k otomastis kiri dan di tambah 1

        while j < len(kanan): #ketika j lebih kecil dari kanan
            A[k]= kanan [j] #a samadengan kanan
            j= j+1 #maka kanan di tambah 1
            k = k +1 #k otomatis kanan dan di tambah 1
        return A
    #print 'menggabungkan' , A
    
def quickSort(a):
    quickSortbantu(a, 0, len(a)-1) #memanggil quickshort bantu
    
def quickSortbantu(a,awal,akhir):
    if awal <akhir:
        titikBelah = partisi (a, awal, akhir) #atur elemen dan dapatkan titik belah
        quickSortbantu(a, awal, titikBelah-1) #ini rekursi untuk belah sisi kiri
        quickSortbantu(a, titikBelah+1, akhir) #dan belah sisi kanan

def partisi(a,awal,akhir):
    nilaiPivot = a[awal].getNim() #nilai pivot di ambil dari elemen yg paling kiri disertai nim
    penandakiri = awal +1 #posisi awal penandakiri
    penandakanan = akhir #posisi awal penanda kanan
    selesai = False

    while not selesai: #loop untuk mengatur ulang posisi semua elemen
        while  penandakiri <= penandakanan and \
            a[penandakiri].getNim() <= nilaiPivot: #sampai ketemu suatu nilai yang
            penandakiri = penandakiri +1 #lebih besar dari nilai pivot
        while  a[penandakanan].getNim() >=nilaiPivot and penandakanan >= penandakiri:
            penandakanan = penandakanan -1
        if penandakanan < penandakiri: #kalau dua penanda sudah bersilangan
            selesai = True #selesai dan lanjut ke penempatan pivot
        else:
            a[penandakiri],a[penandakanan] = a[penandakanan], a[penandakiri]

    a[awal], a[penandakanan] = a[penandakanan], a[awal]
    return penandakanan #fungsi mengembalikan titik belah ke pemanggil

print ("merge sort")
mergesort(daftar) 
for i in daftar:
    print (i) #untuk menampilkan list menggunakan mergesort dari daftar

print(" ")

print ('quick sort')
quickSort(daftar)
for i in daftar:
    print (i) #untuk menampilkan list menggunakan quicksort dari daftar
