N, M = map(int,input().split())
SC = []
for i in range(M):
    sc = list(map(int,input().split()))
    SC.append(sc)

ans = [0] * N
for i in range(M):
    if ans[SC[i][0] - 1] == 0:
        ans[SC[i][0] - 1] = SC[i][1]
    else:
        if ans[SC[i][0] - 1] != SC[i][1]:
            print(-1)
            exit()
if ans[0] == 0:
    print(-1)
    exit()

x = 0        
for i in range(N):
    x += 10 ** (N - i - 1) * ans[i]

if x == 0:
    x = - 1
print(x)