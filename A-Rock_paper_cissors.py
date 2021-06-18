x, y = map(int, input().split())
ans = 0
if x == y:
    ans = x
else:
    if (x == 0 and y == 1) or (x == 1 and y == 0):
        ans = 2
    elif (x == 0 and y == 2) or (x == 2 and y == 0):
        ans = 1
    elif (x == 1 and y == 2) or (x == 2 and y == 1):
        ans = 0

print(ans)

