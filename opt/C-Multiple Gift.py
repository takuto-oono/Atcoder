X, Y = map(int,input().split())
ans = 0
x = X

while x <= Y:
    ans += 1
    x *= 2

print(ans)
    
