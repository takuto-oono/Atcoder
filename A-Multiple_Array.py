n = int(input())

A = []
B = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
ans = 0
for i in range(n):
    x = n - 1 - i
    a = A[x]
    b = B[x]

    m = (a + ans) % b

    if m > 0:
        ans += b - m

print(ans)

    