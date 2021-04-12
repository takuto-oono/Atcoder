import math
n = int(input())
A = list(map(int, input().split()))
ans = A[n - 1]
for i in range(n - 1):
    ans = math.gcd(ans, A[i])


print(ans)