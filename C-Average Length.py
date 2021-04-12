import math
N = int(input())
A = []
for i in range(N):
    xy = list(map(int,input().split()))
    A.append(xy)

x = 0
sum = 0
for i in range(N - 1):
    for j in range(N - 1):
        if i != j:
            x = (A[i][0] - A[i + 1][0]) ** 2 + (A[i][1] - A[i + 1][1]) ** 2
            x = math.sqrt(x)
            sum += x

z = 1
for i in range(2, N - 1):
    z *= i

ans = x / 2 * z

print(ans)


