A ,B = map(int,input().split())
x = 1
ans = 0
while x < B:
    ans += 1
    x = x - 1 + A
print(ans)

    
