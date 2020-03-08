class Manusia(object):
    """Class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = 'lapar'

    def __init__(self, nama):
        self.nama = nama

    def ucapkanSalam(self):
        print('Salam, namaku', self.nama)

    def makan(self, s):
        print('Saya baru saja makan', s)
        self.keadaan = 'kenyang'

    def olahraga(self, k):
        print('Saya baru saja latihan', k)
        self.keadaan = 'lapar'

    def mengalikanDenganDua(self, n):
        return n * 2


class SiswaSMA(Manusia):
    def __init__(self, nama, NISN, alamat, sekolah, us):
        self.nama = nama
        self.NISN = NISN
        self.sekolah = sekolah
        self.alamat = alamat
        self.uangSaku = us
    def __str__(self):
        s = self.nama+ ", No Absen " + str(self.noAbsen) \
            + ". sekolah di " + self.sekolah \
            + ". Uang saku Rp " + str(self.uangSaku) \
            + " tiap minggunya."
        return s
    def ambilNama(self):
        return self.nama
    def ambilNISN(self):
        return self.NISN
    def ambilSekolah(self):
        return self.sekolah
    def ambilAlamat(self):
        return self.alamat
    def perbaruiAlamat(self,x):
        self.alamat = x
    def ambilUangSaku(self):
        return self.uangSaku
    def tambahUangSaku(self,x):
        self.uangSaku += x
