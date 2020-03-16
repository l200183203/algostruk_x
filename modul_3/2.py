#2
def buatNol(m, n):
    """m for row, n for coloumn"""
    matriks = [[0 for j in range(m)] for i in range(n)]
    
    for i in matriks:
        print (i)
    print ("Matriks nol ber ordo",m,'x',n)

def buatNol2(m):
    """m for coloumn and it is square matrix same ordo"""
    matriks = [[0 for j in range(m)] for i in range(m)]
    for i in matriks:
        print (i)
    print ("Matriks nol ber ordo",m,'x',m)

def buatIdentitas(m):
    """Identity Matrix"""
    matriks = [[1 if j == i else 0 for j in range(m)] for i in range(m)]
    for i in matriks:
        print (i)
    print ("Matriks identitas ber ordo",m,'x',m)

buatNol(3,2)
buatNol2(4)
buatIdentitas(4)
