n, m = map(int,input().split())
X = list(map(int,input().split()))
X = sorted(X)
Diffs = []


for i in range(m - 1):
    diff = X[i + 1] - X[i]
    Diffs.append(diff)

Diffs = sorted(Diffs)
ans = 0

for i in range(m - n):
    
    ans += Diffs[i]

print(ans)
