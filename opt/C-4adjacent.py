N = int(input())
A = list(map(int,input().split()))

def hantei(N, A):
    a = 0
    b = 0
    c = 0
    for i in range(N):
        x = A[i]
        if x % 4 == 0:
            a += 1
        elif x % 4 == 2:
            b += 1
        elif x % 4 == 1 or x % 4 == 3:
            c += 1

    if b == 0:
        if a - c >= -1:
            ans = 1
        else:
            ans = 0
    elif b == 1:
        if a - c >= 0:
            ans = 1
        else:
            ans = 0
    else:
        if a - c >= 0:
            ans = 1
        else:
            ans = 0


    return ans

if hantei(N, A) == 1:
    print('Yes')
else:
    print('No') 