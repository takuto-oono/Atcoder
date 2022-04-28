n, m = map(int, input().split())

A = list(map(int, input().split()))
D = []

for i in range(n):
    x = A[i]
    while(x != 0):
        D.append(x - (x // 2))
        x //= 2
ans = sum(A)
if len(D) < m:
    for i in range(m - len(D) + 3):
        D.append(0)
D = sorted(D)
for i in range(m):
    index = len(D) - 1 - i
    ans -= D[index]
print(ans)
