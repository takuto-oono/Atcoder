import math
import statistics
n, k = map(int, input().split())
A = []

for i in range(n):
    a = list(map(int, input().split()))
    A.append(a)
ans = 10 ** 10
for i in range(n - k + 1):
    for j in range(n - k + 1):
        B = []
        for y in range(i, i + k):
            for x in range(j, j + k):
                B.append(A[y][x])
        if n % 2 == 1:
            median = statistics.median(B)
        else:
            median = statistics.median_low(B)
        print(median)
        ans = min(median, ans)


print(ans)

