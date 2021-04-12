N = int(input())
X = list(map(int,input().split()))
P = int(sum(X) / N + 0.5)
ans = 0

for i in range(N):
    ans += (X[i] - P) ** 2

print(ans)

