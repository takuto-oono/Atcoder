n, m = map(int, input().split())
ans = 0
if 2 * n >= m:
    ans = m // 2
else:
    ans = n
    m -= 2 * n
    ans += (m / 4)

ans = int(ans)
print(ans)