x, y = map(int,input().split())
z = abs(x - y)
if z < 3:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)
