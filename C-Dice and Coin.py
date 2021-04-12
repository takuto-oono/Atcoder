N, K =  map(int,input().split())

ans = 0
x = 0
y = 0
for i in range(1,N + 1):
    y = 1 / N
    x = i
    while x < K:
        x *= 2
        y *= 1 / 2
    
    ans += y
print(ans)