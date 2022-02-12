n, m = map(int, input().split())
KS = []
for i in range(m):
    ks = list(map(int, input().split()))
    KS.append(ks)

P = list(map(int, input().split()))

ans = 0
for i in range(2 ** n):
    memo = [0 for k in range(n)]
    for j in range(n):
        if (i >> j) & 1:
            memo[j] = 1

    memo2 = 0
    for h in range(m):
        l = len(KS[h])
        memo1 = 0
        for o in range(1, l):
            if memo[KS[h][o] - 1] == 1:
                memo1 += 1
        if memo1 % 2 == P[h]:
            memo2 += 1

    if memo2 == m:
        ans += 1

print(ans)





