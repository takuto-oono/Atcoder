x, y = map(int,input().split())
ans = 0
if abs(x) < abs(y):
    if x < 0:
        ans += 1
        x = -x
    ans += abs(y) - abs(x)
    x += abs(y) - abs(x)
    if x != y:
        ans += 1
        x = -x
    
elif abs(x) == abs(y):
    if x != y:
        ans += 1

else:
    if x > 0:
        x = -x
        ans += 1
    
    ans += abs(x) - abs(y)
    x += abs(x) - abs(y)
    

    if x != y:
        ans += 1
        x = -x
    
print(ans)



