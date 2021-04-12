a, b = map(int,input().split())
x = min(a, b)
y = max(a, b)
z = [x] * y
ans = ''.join(z)
print(ans)
