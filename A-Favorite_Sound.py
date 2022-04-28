a, b, c = map(int,input().split())
ans = b // a
if ans > c:
    ans = c
print(ans)
