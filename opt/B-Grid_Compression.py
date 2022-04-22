def CHECK_VERTICAL(h, w, A):
    for j in range(w):
        co = 0
        for i in range(h):
            if A[i][j] == '#':
                co += 1
        if co == 0:
            return j
    return -1

def CHECK_SIDE(h, w, A):
    for i in range(h):
        co = 0
        for j in range(w):
            if A[i][j] == '#':
                co += 1
        if co == 0:
            return i
    return -1

h, w  = map(int,input().split())
A = []
for i in range(h):
    a = input()
    a = list(a)
    A.append(a)
x = 1
while(x == 1):
    check_vertical = CHECK_VERTICAL(h, w, A)
    
    if check_vertical != -1:
        for i in range(h):
            del A[i][check_vertical]
        w -= 1

    else:
        check_side = CHECK_SIDE(h, w, A)
        if check_side != -1:
            
            del A[check_side]
            h -= 1
        else:
            x = 0
    

for i in range(h):
    ans = ''
    for j in range(w):
        ans += A[i][j]
    print(ans)
    



