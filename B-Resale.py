n = int(input())
ans = 0
V = list(map(int, input().split()))
C = list(map(int, input().split()))

for i in range(n):
    x = V[i] - C[i]
    if x > 0:
        ans += x

print(ans)
