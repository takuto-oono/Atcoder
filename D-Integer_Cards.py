n, m = map(int, input().split())
A = list(map(int, input().split()))

BC = []
for i in range(m):
    b, c = map(int, input().split())
    BC.append([c, b])

A = sorted(A)
BC = sorted(BC, reverse=True)
ans = sum(A)
i = 0
for (c, b) in BC:
    memo = 0
    while i < n and memo < b and A[i] < c:
        ans += (c - A[i])
        memo += 1
        i += 1

print(ans)


