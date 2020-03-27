a=[12,23,41,56,22,86]
b=[32,43,9,4,29,84]

def swap(x,a,b):
    temp=x[a]
    x[a]=x[b]
    x[b]=temp

def sort(x,y):
    a=[]
    m=len(y)
    for i in range(m):
        a.append(y[i])
    n=len(x)
    for i in range(n):
        a.append(x[i])
        
    o=len(a)
    for i in range(o-1):
        for j in range(o-i-1):
            if a[j]>a[j+1]:
                swap(a,j,j+1)
    print(a)

sort(a,b)
