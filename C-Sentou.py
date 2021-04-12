N, t = map(int,input().split())
T = list(map(int,input().split()))

ans = 0
for i in range(N):
    if i != 0:
        x = T[i] - T[i - 1]
        ans += min(t, x)

    if i == N - 1:
        ans += t

print(ans)



