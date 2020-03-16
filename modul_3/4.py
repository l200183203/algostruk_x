#4
class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    def listPrint(self):
        isi = self.head
        tempat = []
        while isi is not None:
            tempat.append(isi.data)
            isi = isi.next
        print(tempat)
    def tampilkan(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next
    def tambahDepan(self, a):
        a.next = self.head
        self.head = a
    def tambahAkhir(self, b):
        self.tail.next = b
        self.tail = b
            
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
linked.tampilkan()

#Nomer2
print("Hasil nomor 2")
x = Node(60)
linked.tambahDepan(x)
linked.listPrint()

#Nomer3
print("Hasil nomor 3")
y = Node(70)
linked.tambahAkhir(y)
linked.listPrint()
