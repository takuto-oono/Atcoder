a, b, c, d = map(int,input().split())
x = a * c
y = a * d
z = b * c
u = b * d
ans = max(x, y, z, u)
print(ans)