N, M, T = map(int,input().split())
L = N
c = 0
t = []
for i in range(M):
    ab = list(map(int,input().split()))
    t.append(ab)

for i in range(M):
    if i == 0:
        L -= t[0][0]
        if L <= 0:
            c = 1
            break
        L += (t[0][1] - t[0][0])
        if L > N:
            L = N
        if i == M - 1:
            L -= (T - t[i][1])
            if L <= 0:
                c = 1
                break
    else:
        L -= (t[i][0] - t[i - 1][1])
        if L <= 0:
            c = 1
            break
        L += (t[i][1] - t[i][0])
        if L > N:
            L = N
        if i == M - 1:
            L -= (T - t[i][1])
            if L <= 0:
                c = 1
                
if c == 0:
    print('Yes')
else:
    print('No')

        

    