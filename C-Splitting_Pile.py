n = int(input())
A = list(map(int, input().split()))

A_sum = sum(A)
x = A[0]
y = A_sum - A[0]
ans = abs(x - y)

for i in range(1, n - 1):
    x += A[i]
    y -= A[i]
    ans = min(ans, abs(x - y))

print(ans)
