class Pesan(object):
    """
        Sebuah class bernama pesan.
        Untuk memahami konsep Class dan Object.
    """
    def __init__(self,sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumkar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('kalimatku mempunyai',len(self.teks),'karakter.')
    def perbarui(self,stringBaru):
        self.teks = stringBaru
#a
    def __init__ (self, p):
        self.pesan = p
        
    def apakahTerkandung(self, cari):
        if cari in self.pesan:
            return True
        else:
            return False

    def cetakPesan(self):
        return self.pesan
#b
    def hitungKonsonan(self):     
        vokal = "aioueAIOUE"
        hitung = 0
        for i in self.pesan:
            if i not in vokal:
                hitung += 1
        return hitung
#c    
    def hitungVokal(self):
        vokal = "aioueAIOUE"
        hitung = 0
        for i in self.pesan:
            if i in vokal:
                hitung += 1
        return hitung
    
    
