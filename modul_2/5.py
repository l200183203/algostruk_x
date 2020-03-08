class Mahasiswa(object):
    """ Class Mahasiswa yang dibangun dari class Manusia """
    def __init__(self, nama, NIM, kota,us,kuliah):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        self.listKuliah = []
        self.kuliah = kuliah
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
           + '. Tinggal di ' + self.kotaTinggal \
           + '. Uang saku Rp ' + str(self.uangSaku) \
           + '. tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self,s):
        """Metode ini menutupi 'makan'-nya class Manusia.
        Mahasiswa kalau makan sambl belajar."""
        print ("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan = 'kenyang'
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self,x):
        self.kotaTinggal = x
    def tambahUangSaku(self,x):
        self.uangSaku += x
    def ListKuliah(self):
        return self.listKuliah
    def ambilKuliah(self, tambahKuliah):
        self.listKuliah.append(tambahKuliah)
    def hapusListKuliah(self, hapusKuliah):
        for i in self.listKuliah:
            if hapusKuliah in self.listKuliah:
                self.listKuliah.remove(hapusKuliah)
            else:
                print("Im sorry your subject doesnt appear in this list")


