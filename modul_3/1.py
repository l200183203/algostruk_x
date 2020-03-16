#1
a = [1,2,3,4]
b = [1, "a", 2, "b", 3]
c = [[1, 2], [3, 4], [5, 6]]
d = [[1, "a"], [2, "b"], [3, "c"]]
e = [[1, 2], 3, [4, 5, 6]]
f = [[1, "a"], 2, ["b", 5, "c"]]
t = [[1,2,3], [4,5,6], [7,8,9]]
s = [[1,2],[3,4]]
u = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
g = []
r = []

#mengecek matrix
def cek(x):
    for i in x:
        g.append(type(i))
    if list in g:
        h = len(x[0])
        k = type(x[0][0])
        try:
            for i in x:
                if len(i) != h:
                    del(g[:])
                    raise AssertionError("Ukuran matrix tidak konsisten")
                else:
                    pass
            for i in x:
                for j in i:
                    if type(j) != k:
                        del(g[:])
                        raise AssertionError("Isi matrix tidak konsisten")
                    else:
                        pass
        except TypeError:
            del(g[:])
            raise AssertionError("Ukuran matrix tidak konsisten")
        print("Ukuran dan isi matrix konsisten")
        del(g[:])
    else:
        m = type(x[0])
        for i in x:
            if type(i) != m:
                del(g[:])
                raise AssertionError("Isi matrix tidak konsisten")
            else:
                pass
        print("Ukuran dan isi matrix konsisten")
        del(g[:])

#mengambil ukuran matrix    
def ukuran(x):
    for i in x:
        g.append(type(i))
    if list in g:
        h = len(x[0])
        try:
            for i in x :
                if len(i) != h:
                    del(g[:])
                    raise AssertionError("Ukuran matrix tidak konsisten")
                else:
                    pass
        except TypeError:
            del(g[:])
            raise AssertionError("Ukuran matrix tidak konsisten")
        print(str(len(x)) + "x" + str(len(x[0])))
        del(g[:])
    else:
        print(str(len(x)) + "x" + "1")
        del(g[:])

#menjumlahkan 2matrix
def jumlah(x,y):
    for i in x:
        g.append(type(i))
    if list in g:
        h = len(x[0])
        try:
            for i in x:
                if len(i) != h:
                    del(g[:])
                    raise AssertionError("Ukuran matrix tidak konsisten")
                else:
                    pass
        except TypeError:
            del(g[:])
            raise AssertionError("Ukuran matrix tidak konsisten")
        del(g[:])
        for i in y:
            g.append(type(i))
        if list in g:
            try:
                l = len(x)
                for i in y:
                    if len(i) != h or len(y) != len(x):
                        del(g[:])
                        raise AssertionError("Ukuran matrix tidak konsisten dan tidak sama")
                    else:
                        pass
            except TypeError:
                del(g[:])
                raise AssertionError("Ukuran matrix tidak sama")
            o = 0
            for i in x:
                n = 0
                q = []
                for j in i:
                    j += y[o][n]
                    n += 1
                    q.append(j)
                r.append(q)
                o += 1
            print(r)
            del(g[:])
        else:
            del(g[:])
            raise AssertionError("Ukuran kedua matrix tidak sama")
    else:
        try:
            o = 0
            for i in x:
                i += y[o]
                o += 1
                r.append(i)
            print(r)
            del(g[:])
        except TypeError:
            del(g[:])
            raise AssertionError("Ukuran matrix tidak sama")

#mengalikan dua matrix        
def kali(x,y):
    for i in x:
        g.append(type(i))
    if list in g:
        h = len(x[0])
        try:
            for i in x:
                if len(i) != h:
                    del(g[:])
                    raise AssertionError("Ukuran matrix tidak konsisten")
                else:
                    pass
        except TypeError:
            del(g[:])
            raise AssertionError("Ukuran matrix tidak konsisten")
        del(g[:])
        for i in y:
            g.append(type(i))
        if list in g:
            try:
                l = len(x)
                for i in y:
                    if len(i) != h or len(y) != len(x):
                        del(g[:])
                        raise AssertionError("Ukuran matrix tidak konsisten dan tidak sama")
                    else:
                        pass
            except TypeError:
                del(g[:])
                raise AssertionError("Ukuran matrix tidak sama")
            try:
                o = 0
                for i in x:
                    n = 0
                    q = []
                    for j in i:
                        j *= y[o][n]
                        n += 1
                        q.append(j)
                    r.append(q)
                    o += 1
                print(r)
                del(g[:])
            except TypeError:
                del(g[:])
                raise AssertionError("Terdapat perkalian String dengan String")
        else:
            del(g[:])
            raise AssertionError("Ukuran kedua matrix tidak sama")
    else:
        try:
            o = 0
            for i in x:
                i *= y[o]
                o += 1
                r.append(i)
            print(r)
            del(g[:])
        except TypeError:
            del(g[:])
            raise AssertionError("Ukuran matrix tidak sama atau terdapat perkalian String dengan String")

#menghitung determinan
def determinan(x):
    if len(x) != len(x[0]):
        raise AssertionError("Bukan matrix bujur sangkar")
    elif len(x) == 2:
        try:
            print(((x[0][0])*(x[1][1]))-((x[1][0])*(x[0][1])))
        except TypeError:
            raise AssertionError("Terdapat perkalian String dengan String")
    elif len(x) == 3:
        try:
            print(((x[0][0])*(x[1][1])*(x[2][2]))+((x[1][0])*(x[2][1])*(x[0][2]))+((x[2][0])*(x[0][1])*(x[1][2]))-((x[2][0])*(x[1][1])*(x[0][2]))-((x[1][0])*(x[0][1])*(x[2][2]))-((x[0][0])*(x[2][1])*(x[1][2])))
        except TypeError:
            raise AssertionError("Terdapat perkalian String dengan String")
    else:
        raise AssertionError("Ukuran matrix tidak boleh lebih dari 3x3")
