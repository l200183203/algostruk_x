# nomer 7

from time import time as detak
from random import shuffle as kocok
import time

#MERGE SORT LAMA
def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]

        mergeSort(separuhKiri)
        mergeSort(separuhKanan)

        i = 0 ; j = 0 ; k = 0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i] < separuhKanan[j]:
                A[k] = separuhKiri[i]
                i += 1
            else:
                A[k] = separuhKanan[j]
                j += 1
            k += 1

        while i < len(separuhKiri):
            A[k] = separuhKiri[i]
            i += 1
            k += 1

        while j < len(separuhKanan):
            A[k] = separuhKanan[j]
            j += 1
            k += 1

#MERGE SORT BARU
def merge_sort(A, B):
    start = A[0]
    end = A[1]
    mid = (end - start) // 2 + start
    
    if start < mid:
        merge_sort((start, mid), B)

    if mid + 1 <= end and end - start != 1:
       merge_sort((mid + 1, end), B)

    subList(B, A[0], A[1])
    return B

      
def subList(B, start, end):
    mulai = start
    List = (end - start)//2 + start + 1
    List2 = List
    new_list = []
    
    while start < List and List2 <= end:
        first1 = B[start]
        first2 = B[List2]
        if first1 > first2:
            new_list.append(first2)
            List2 += 1
        else:
            new_list.append(first1)
            start += 1
            
    while start < List :
        new_list.append(B[start])
        start += 1

    while List2 <= end:
        new_list.append(B[List2])
        List2 += 1
        
    for i in new_list:
        B[mulai] = i
        mulai += 1
        
    return B

def mergeSort_new(B):
    return merge_sort((0, len(B) - 1), B)


#QUICK SORT LAMA
def partisi(A, awal, akhir):
    nilaiPivot = A[awal]

    penandaKiri = awal + 1
    penandaKanan = akhir

    selesai = False
    while not selesai:

        while penandaKiri <= penandaKanan and \
              A[penandaKiri] <= nilaiPivot:
            penandaKiri = penandaKiri + 1

        while A[penandaKanan] >= nilaiPivot and \
              penandaKanan >= penandaKiri:
            penandaKanan = penandaKanan - 1

        if penandaKanan < penandaKiri:
            selesai = True
        else:
            temp = A[penandaKiri]
            A[penandaKiri] = A[penandaKanan]
            A[penandaKanan] = temp

    temp = A[awal]
    A[awal] = A[penandaKanan]
    A[penandaKanan] = temp

    return penandaKanan
    
def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah - 1)
        quickSortBantu(A, titikBelah + 1, akhir)

def quickSort_new(A):
    quickSortBantu(A, 0, len(A) - 1)

#QUICK SORT BARU
def quickSort(L, ascending = True): 
    QShelp(L, 0, len(L), ascending)
    
def QShelp(L, low, high, ascending = True): 
    result = 0
    if low < high: 
        pivot_location, result = Partition(L, low, high, ascending)  
        result += QShelp(L, low, pivot_location, ascending)  
        result += QShelp(L, pivot_location + 1, high, ascending)
    return result


def Partition(L, low, high, ascending = True):
    result = 0 
    pivot, pidx = mot(L, low, high)
    L[low], L[pidx] = L[pidx], L[low]
    i = low + 1
    for j in range(low + 1, high, 1):
        result += 1
        if (ascending and L[j] < pivot) or (not ascending and L[j] > pivot):
            L[i], L[j] = L[j], L[i]  
            i += 1
    L[low], L[i - 1] = L[i - 1], L[low] 
    return i - 1, result


# Median Of Three
def mot(L, low, high):
    mid = (low + high - 1) // 2
    a = L[low]
    b = L[mid]
    c = L[high - 1]
    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, high - 1
    if b <= c <= a:
        return c, high - 1
    return a, low

k = list(range(6000))
kocok(k)
u_mrg = k[:]
u_qck = k[:]
u_mrg_new = k[:]
u_qck_new = k[:]

aw = detak();mergeSort(u_mrg);ak = detak();print('Merge : %g detik' %(ak-aw));
aw = detak();quickSort(u_qck);ak = detak();print('Quick : %g detik' %(ak-aw));
aw = detak();mergeSort_new(u_mrg_new);ak = detak();print('Merge New : %g detik' %(ak-aw));
aw = detak();quickSort_new(u_qck_new);ak = detak();print('Quick New : %g detik' %(ak-aw));


### HASIL
##Merge : 0.059263 detik
##Quick : 0.0351264 detik
##Merge New : 0.0471561 detik
##Quick New : 0.0270734 detik
