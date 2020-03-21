#No. 7
B = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
def binSe2(target):
    low = 0
    high = len(B)
    x = []

    while low < high:
        if B[low] == target:
            x.append(low)
            low+=1
        else:
            low+=1
    return x
