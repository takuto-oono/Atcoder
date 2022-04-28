n, m = map(int,input().split())

if (n == 1 and m == 1) or (n != 1 and m != 1):
    ans = m * n - (2 * (m - 1) + 2 * (n - 1))
else:
    ans = max(m, n) - 2
print(ans)

