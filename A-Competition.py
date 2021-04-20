x, y, z = map(int, input().split())

ans = y * z / x

if int(ans) == ans:
    ans -= 1
    ans = int(ans)
else:
    ans = int(ans)

print(ans)
