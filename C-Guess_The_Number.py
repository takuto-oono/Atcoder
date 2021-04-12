n, m = map(int,input().split())
ans = ['0' for i in range(n)]
SC = []
for i in range(m):
    sc = list(map(int,input().split()))
    SC.append(sc)

SC = sorted(SC)
for i in range(m - 1):
    if SC[i][0] == SC[i + 1][0]:
        if SC[i][1] != SC[i + 1][1]:
            print(-1)
            exit()

for i in range(1000):
    X = str(i)
    
    l = len(X)
    co = 0
    for j in range(m):
        if SC[j][0] <= l:
            if X[SC[j][0] - 1] == str(SC[j][1]):
                co += 1
    if co == m:
        if l == n:
            ans = X
            print(ans)
            exit()

print(-1)

        



