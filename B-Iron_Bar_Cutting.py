n = int(input())
A = list(map(int,input().split()))
length = sum(A)
x = 10 ** 11
y = 0
if length % 2 == 0:
    for i in range(n):
        y += A[i]
        x = min(x, abs(length // 2 - y))
    ans = 2 * x
else:
    x = 10 ** 11
    y = 0
    for i in range(n):
        y += A[i]
        x = min(x, abs(length // 2 - y))
        x = min(x, abs(length // 2 - y + 1))
    ans = 2 * x + 1
    




print(ans)
    