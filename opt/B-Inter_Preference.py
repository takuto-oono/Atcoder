a, b, c, d = map(int,input().split())
e = max(a, c)
f = min(b, d)
if f - e >= 0:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)
