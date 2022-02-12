import math
N, x = map(int,input().split())
X = list(map(int,input().split()))
y = []
X.append(x)
X = sorted(X)

for i in range(N):
    a = X[i + 1] - X[i]
    y.append(a)
ans = y[0]
for i in range(N):
    ans = math.gcd(ans, y[i])

print(ans) 