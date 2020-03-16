#3
class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
class LinkedList():
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    def listprint(self):
        printval = self.head
        hasil = []
        while printval is not None:
            hasil.append(printval.data)
            printval = printval.next
        print(hasil)
    def cari(self, nilai):
        cek = self.head
        a = 1
        while cek is not None:
            if cek.data == nilai:
                print("terdapat pada urutan ke-"+str(a))
                break
            if cek.data != nilai:
                a += 1
                cek = cek.next
    def tambahDepan(self, b):
        b.next = self.head
        self.head = b
    def tambahAkhir(self, c):
        self.tail.next = c
        self.tail = c
    def tambah(self, d, posisi):
        if posisi == 1:
            d.next = self.head
            self.head = d
        if posisi == 7:
            self.tail.next = d
            self.tail = d
        if posisi == 2:
            d.next = self.head.next
            self.head.next = d
        if posisi == 3:
            d.next = self.head.next.next
            self.head.next.next = d
        if posisi == 4:
            d.next = self.head.next.next.next
            self.head.next.next.next = d
        if posisi == 5:
            d.next == self.head.next.next.next.next
            self.head.next.next.next.next = d
        if posisi == 6:
            d.next == self.head.next.next.next.next.next
            self.head.next.next.next.next.next = d
        if posisi > 7 or posisi < 0:
            raise AssertionError("Posisi harus direntang 0 sampai 7")
    def hapus(self, posisi): 
        hapus = self.head 
        if posisi == 0: 
            self.head = temp.next
            hapus = None
        for i in range(posisi-1): 
            hapus = hapus.next
            if hapus is None: 
                break
        next = hapus.next.next
        hapus.next = next 
        
        
a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)
e = Node(50)

a.next = b
b.next = c
c.next = d
d.next = e

linked = LinkedList()
linked.head = a
linked.tail = e

#Nomer1
print("Hasil nomor 1")
linked.listprint()
linked.cari(20) 

#Nomer2
print("Hasil nomor 2")
x = Node(60)
linked.tambahDepan(x)
linked.listprint()
print(linked.head.data)

#Nomer3
print("Hasil nomor 3")
y = Node(70)
linked.tambahAkhir(y)
linked.listprint()
print(linked.tail.data)

#Nomer4
print("Hasil nomor 4")
z = Node(80)
linked.tambah(z,2)
linked.listprint()
print(linked.head.next.data)

#Nomer5
print("Hasil nomor 5")
linked.hapus(1)
linked.listprint()
