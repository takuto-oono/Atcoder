S = input()
A = S[0:2]
B = S[2:4]
A = int(A)
B = int(B)

def hantei(x, y):
    a = 0
    b = 0
    if 0 < x <= 12:
        a = 1
    if 0 < y <= 12:
        b = 1
    
    if a == 1 and b == 1:
        ans = 'AMBIGUOUS'
    elif a == 1 and b == 0:
        ans == 'MMYY'
    elif a == 0 and b == 1:
        ans = 'YYMM'
    else:
        ans = 'NA'
    
    return ans

print(hantei(A, B))


