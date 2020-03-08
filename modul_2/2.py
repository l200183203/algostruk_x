class Mahasiswa(object):
    """ Class Mahasiswa yang dibangun dari class Manusia """
    def __init__(self,nama,NIM,kota,us):
        """Metode inisiasi ini menutupi metode inisisasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
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
#a
    def ambilKotaTinggal(self):
        return self.kotaTinggal
#b
    def perbaruiKotaTinggal(self,x):
        self.kotaTinggal = x
#c
    def tambahUangSaku(self,x):
        self.uangSaku += x
