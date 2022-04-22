N = int(input())
T = list(map(int,input().split()))
M = int(input())
ans = 0
b = []
for j in range(M):
    P, X = map(int,input().split())
    for i in range(N):
        if i + 1 == P:
            ans += X
        else:
            ans += T[i]
    b.append(ans)
    ans = 0
for i in range(M):
    print(b[i])
