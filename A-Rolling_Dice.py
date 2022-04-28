a, b = map(int, input().split())
ans = ''

if a <= b <= 6 * a:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
