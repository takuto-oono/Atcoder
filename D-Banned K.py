N = int(input())
A = list(map(int,input().split()))
import collections

co = collections.Counter(A)
ans = 0

for i in co:
    ans += co[i] * (co[i] - 1)
ans //= 2

for i in range(N):
    print(ans - (co[A[i]] - 1))
